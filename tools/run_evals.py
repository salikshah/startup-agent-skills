#!/usr/bin/env python3
"""Run per-skill evals from skills/<category>/<skill>/evals/evals.json.

Modes:
  static (default)  No network. Checks each assertion's concepts appear in the
                    skill's SKILL.md and references/. Reports coverage.
  --llm             Calls the Anthropic API (ANTHROPIC_API_KEY) to answer the
                    prompt with the skill loaded, then judges each assertion.
                    Reports pass rate.

Exit non-zero if any skill's score is below --threshold (default 0.8 in LLM mode,
0.5 in static mode). No third-party dependencies.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_skills import ROOT, skill_dirs  # noqa: E402

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "than", "that", "this",
    "with", "for", "from", "into", "onto", "about", "should", "must", "will",
    "would", "could", "can", "may", "might", "have", "has", "had", "not", "are",
    "is", "was", "were", "be", "been", "being", "to", "of", "in", "on", "at",
    "by", "as", "it", "its", "they", "them", "their", "you", "your", "we", "our",
    "does", "do", "did", "so", "such", "any", "all", "each", "every", "which",
    "who", "what", "when", "where", "why", "how", "use", "using", "used",
}


def load_evals(skill_dir: Path):
    path = skill_dir / "evals" / "evals.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("evals"), list):
        raise ValueError("evals.json missing 'evals' list")
    return data


def skill_text(skill_dir: Path) -> str:
    parts = [skill_dir.joinpath("SKILL.md").read_text(encoding="utf-8")]
    for ref in skill_dir.rglob("references/**/*.md"):
        parts.append(ref.read_text(encoding="utf-8"))
    return "\n".join(parts)


def significant_terms(text: str):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {w for w in words if len(w) >= 4 and w not in STOPWORDS}


def static_eval(skill_dir: Path, evals):
    text = skill_text(skill_dir)
    terms = significant_terms(text)
    results = []
    for ev in evals["evals"]:
        assertions = ev.get("assertions", [])
        covered = 0
        for assertion in assertions:
            a_terms = significant_terms(assertion)
            if not a_terms or len(a_terms & terms) >= max(1, len(a_terms) // 3):
                covered += 1
        results.append({
            "id": ev.get("id"),
            "assertions": len(assertions),
            "covered": covered,
            "coverage": round(covered / len(assertions), 2) if assertions else 0.0,
        })
    return results


def call_claude(api_key: str, model: str, system: str, user: str, max_tokens: int = 2048) -> str:
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    return payload["content"][0]["text"]


def llm_eval(skill_dir: Path, evals, api_key: str, model: str):
    instructions = skill_text(skill_dir)
    results = []
    for ev in evals["evals"]:
        assertions = ev.get("assertions", [])
        response = call_claude(
            api_key,
            model,
            system=instructions,
            user=str(ev.get("prompt", "")),
        )
        judge_prompt = (
            "You are grading an AI agent's response to a user request.\n\n"
            f"User request:\n{ev.get('prompt', '')}\n\n"
            f"Agent response:\n{response}\n\n"
            f"Expected output:\n{ev.get('expected_output', '')}\n\n"
            "For each assertion below, decide whether the agent response satisfies it. "
            "Return only JSON: {\"passed\": [indices], \"failed\": [indices]}\n"
            + "\n".join(f"{i}. {a}" for i, a in enumerate(assertions))
        )
        raw = call_claude(
            api_key,
            model,
            system="You are a strict evaluator. Return only JSON.",
            user=judge_prompt,
            max_tokens=1024,
        )
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        verdict = json.loads(match.group(0)) if match else {"passed": [], "failed": list(range(len(assertions)))}
        passed = len(verdict.get("passed", []))
        results.append({
            "id": ev.get("id"),
            "assertions": len(assertions),
            "passed": passed,
            "coverage": round(passed / len(assertions), 2) if assertions else 0.0,
        })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["static", "llm"], default="static")
    parser.add_argument("--llm", action="store_true", help="shorthand for --mode llm")
    parser.add_argument("--model", default=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-5"), help="Anthropic model for LLM mode")
    parser.add_argument("--threshold", type=float, default=None, help="pass threshold (0-1)")
    parser.add_argument("--json", type=Path, default=ROOT / "reports" / "evals.json")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    mode = "llm" if args.llm else args.mode
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if mode == "llm" and not api_key:
        raise SystemExit("LLM mode needs ANTHROPIC_API_KEY in the environment")

    threshold = args.threshold if args.threshold is not None else (0.8 if mode == "llm" else 0.5)
    report = []
    for skill_dir in skill_dirs():
        evals = load_evals(skill_dir)
        if mode == "llm":
            results = llm_eval(skill_dir, evals, api_key, args.model)
        else:
            results = static_eval(skill_dir, evals)
        total_assertions = sum(r["assertions"] for r in results)
        total_pass = sum(r.get("covered", r.get("passed", 0)) for r in results)
        score = round(total_pass / total_assertions, 2) if total_assertions else 0.0
        report.append({
            "skill": skill_dir.name,
            "evals": len(evals["evals"]),
            "assertions": total_assertions,
            "score": score,
            "results": results,
        })

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Mode: {mode}  Threshold: {threshold}")
    print(f"{'Skill':<34} {'Evals':>5} {'Assert':>7} {'Score':>7}")
    print("-" * 57)
    for r in report:
        flag = "PASS" if r["score"] >= threshold else "FAIL"
        print(f"{r['skill']:<34} {r['evals']:>5} {r['assertions']:>7} {r['score']:>6.0%} {flag}")
    if args.verbose:
        for r in report:
            print(f"\n{r['skill']}")
            for res in r["results"]:
                print(f"  eval {res['id']}: {res.get('covered', res.get('passed'))}/{res['assertions']}")

    failures = [r["skill"] for r in report if r["score"] < threshold]
    if failures:
        print(f"\nFAIL: " + ", ".join(f"`{f}`" for f in failures))
        return 1
    print(f"\nPASS: all {len(report)} skills meet {threshold:.0%}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
