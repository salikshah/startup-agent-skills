#!/usr/bin/env python3
"""Score every skill against a deterministic 100-point quality rubric.

The rubric is rule-based and transparent: every point is earned by a checkable
property of the SKILL.md file, so the score is reproducible and auditable.

Dimensions (total 100):
  Spec Compliance      15
  Intent & Triggering  10
  Input/Output Contract 15
  Process Rigor        20
  Evidence & Sourcing  10
  Actionability        15
  Measurement          10
  Anti-Patterns & Scope 5

Default ship threshold: 80. See docs/BENCHMARKS.md.

No third-party dependencies. Writes reports/benchmark.json and reports/benchmark.md.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_skills import ROOT, parse_frontmatter, skill_dirs  # noqa: E402

THRESHOLD = 80

REQUIRED_SECTIONS = [
    "Intent",
    "Inputs",
    "Process (SOP)",
    "Outputs",
    "Evidence",
    "Examples",
    "Metrics",
    "Anti-Patterns",
]


def section(body: str, name: str) -> str:
    pattern = rf"^##\s+{re.escape(name)}\s*$([\s\S]*?)(?=^##\s|\Z)"
    match = re.search(pattern, body, re.MULTILINE)
    return match.group(1) if match else ""


def count_numbered_steps(text: str) -> int:
    return len(re.findall(r"^\s*\d+\.\s+", text, re.MULTILINE))


def has_any(text: str, words) -> bool:
    low = text.lower()
    return any(word in low for word in words)


def score_skill(skill_dir: Path):
    name = skill_dir.name
    text = skill_dir.joinpath("SKILL.md").read_text(encoding="utf-8")
    breakdown = {}

    try:
        data, body = parse_frontmatter(text)
    except ValueError as exc:
        return {"skill": name, "score": 0, "error": str(exc), "breakdown": {}}

    # --- Spec Compliance (15) ---
    fm_ok = isinstance(data.get("name"), str) and isinstance(data.get("description"), str)
    breakdown["Spec Compliance"] = {
        "frontmatter_valid": 5 if fm_ok else 0,
        "name_valid": 3 if bool(data.get("name")) else 0,
        "description_triggers": 4 if has_any(str(data.get("description", "")), ("when", "use", "mention")) else 0,
        "under_500_lines": 3 if len(text.splitlines()) < 500 else 0,
    }

    # --- Intent & Triggering (10) ---
    intent = section(body, "Intent").strip()
    triggers = data.get("triggers", [])
    triggers = triggers if isinstance(triggers, list) else []
    breakdown["Intent & Triggering"] = {
        "intent_present": 5 if len(intent) >= 30 else 0,
        "triggers_ge_3": 5 if len(triggers) >= 3 else 0,
    }

    # --- Input/Output Contract (15) ---
    inputs = section(body, "Inputs").strip()
    outputs = section(body, "Outputs").strip()
    has_template = bool(re.search(r"```", body)) or "Output Format" in body or "## Output" in body
    breakdown["Input/Output Contract"] = {
        "inputs_present": 5 if inputs else 0,
        "outputs_present": 5 if outputs else 0,
        "output_template": 5 if has_template else 0,
    }

    # --- Process Rigor (20) ---
    process = section(body, "Process (SOP)")
    steps = count_numbered_steps(process)
    decisions = has_any(process, ("decide", "if ", "choose", "pivot", "or ", "unless"))
    sequential = steps >= 3 and bool(re.match(r"^\s*1\.", process, re.MULTILINE))
    edge_cases = has_any(process, ("edge case", "edge cases", "if not", "unless", "except", "when to stop", "when not to"))
    breakdown["Process Rigor"] = {
        "steps_ge_5": 5 if steps >= 5 else (3 if steps >= 3 else 0),
        "decision_points": 5 if decisions else 0,
        "sequential": 5 if sequential else 0,
        "edge_cases": 5 if edge_cases else 0,
    }

    # --- Evidence & Sourcing (10) ---
    evidence = section(body, "Evidence")
    cites = bool(re.search(r"by\s+[A-Z]", evidence)) or ('"' in evidence) or ("Source" in evidence) or ("source" in evidence)
    breakdown["Evidence & Sourcing"] = {
        "evidence_present": 5 if evidence.strip() else 0,
        "cites_source": 5 if cites else 0,
    }

    # --- Actionability (15) ---
    examples = section(body, "Examples")
    has_numbers = bool(re.search(r"\d", examples))
    has_checklist = has_any(body, ("- [ ]", "checklist", "template", "```", "worksheet"))
    metrics_text = section(body, "Metrics")
    has_targets = has_any(metrics_text, ("target", "%", ">=", "<=", "goal")) or bool(re.search(r"\d", metrics_text))
    breakdown["Actionability"] = {
        "examples_with_numbers": 5 if (examples.strip() and has_numbers) else 0,
        "checklist_or_template": 5 if has_checklist else 0,
        "metrics_with_targets": 5 if has_targets else 0,
    }

    # --- Measurement (10) ---
    metrics = section(body, "Metrics").strip()
    breakdown["Measurement"] = {
        "metrics_present": 5 if metrics else 0,
        "measurable_targets": 5 if has_targets else 0,
    }

    # --- Anti-Patterns & Scope (5) ---
    anti = section(body, "Anti-Patterns")
    anti_items = len(re.findall(r"^\s*[-*]\s+", anti, re.MULTILINE))
    breakdown["Anti-Patterns & Scope"] = {"three_or_more": 5 if anti_items >= 3 else (3 if anti_items >= 1 else 0)}

    total = sum(sum(d.values()) for d in breakdown.values())
    return {"skill": name, "score": total, "breakdown": breakdown}


def render_markdown(results, threshold):
    lines = [
        "# Benchmark report",
        "",
        f"Threshold: **{threshold}/100**. Generated by `tools/benchmark.py`.",
        "",
        "| Skill | Score | Verdict |",
        "|---|---|---|",
    ]
    for r in sorted(results, key=lambda x: x["score"]):
        verdict = "PASS" if r["score"] >= threshold else "FAIL"
        lines.append(f"| `{r['skill']}` | {r['score']}/100 | {verdict} |")
    lines.append("")
    lines.append("## Dimension reference")
    lines.append("")
    lines.append("| Dimension | Points |")
    lines.append("|---|---|")
    for dim, pts in [
        ("Spec Compliance", 15),
        ("Intent & Triggering", 10),
        ("Input/Output Contract", 15),
        ("Process Rigor", 20),
        ("Evidence & Sourcing", 10),
        ("Actionability", 15),
        ("Measurement", 10),
        ("Anti-Patterns & Scope", 5),
    ]:
        lines.append(f"| {dim} | {pts} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--threshold", type=int, default=THRESHOLD, help="ship threshold (default 80)")
    parser.add_argument("--json", type=Path, default=ROOT / "reports" / "benchmark.json")
    parser.add_argument("--markdown", type=Path, default=ROOT / "reports" / "benchmark.md")
    parser.add_argument("--verbose", action="store_true", help="print per-dimension breakdown")
    args = parser.parse_args()

    results = [score_skill(skill_dir) for skill_dir in skill_dirs()]
    results.sort(key=lambda r: r["score"])

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(results, indent=2), encoding="utf-8")
    args.markdown.write_text(render_markdown(results, args.threshold), encoding="utf-8")

    print(f"{'Skill':<34} {'Score':>6}")
    print("-" * 42)
    for r in results:
        print(f"{r['skill']:<34} {r['score']:>5}/100")
    print("-" * 42)
    if args.verbose:
        for r in results:
            print(f"\n{r['skill']}")
            for dim, checks in r.get("breakdown", {}).items():
                earned = sum(checks.values())
                print(f"  {dim}: {earned}")
                for check, pts in checks.items():
                    print(f"    {'+' if pts else '-'} {check}: {pts}")

    failures = [r["skill"] for r in results if r["score"] < args.threshold]
    if failures:
        print(f"\nFAIL: {len(failures)} skill(s) below {args.threshold}: " + ", ".join(f"`{f}`" for f in failures))
        return 1
    print(f"\nPASS: all {len(results)} skills score >= {args.threshold}/100")
    return 0


if __name__ == "__main__":
    sys.exit(main())
