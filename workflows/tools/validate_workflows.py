#!/usr/bin/env python3
"""Validate every automation workflow under workflows/ (zero dependencies).

Checks for each n8n export (workflows/n8n/**/*.json):
  1. The file parses as JSON and has a non-empty `nodes` list and a `connections` object.
  2. Every node has a unique name, a well-formed `type` (e.g. n8n-nodes-base.webhook,
     @n8n/n8n-nodes-langchain.agent or a community package), a numeric typeVersion,
     a [x, y] position and a parameters object.
  3. Every connection source and target is an existing node, using a known connection
     kind (main or ai_*), every non-sticky node is wired to something, and every
     $('Node name') used in an expression names a node in the same workflow.
  4. No secrets: credential IDs must be the placeholder, and the text must not contain
     API keys, bearer tokens, bot tokens, private keys or literal secret header values.
  5. A matching <slug>.md sits next to the JSON and has a "Source and license" section.

Activepieces files (workflows/activepieces/**): every .json parses and has a matching .md.

Prints a table and exits non-zero on any failure.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WF_DIR = Path(__file__).resolve().parents[1]

PLACEHOLDER_IDS = {"REPLACE_WITH_YOUR_CREDENTIAL_ID", "", None}
TYPE_RE = re.compile(r"^(?:@[a-z0-9][\w.-]*/)?n8n-nodes-[\w.-]+\.[A-Za-z][\w]*$")
CONN_KIND_RE = re.compile(r"^(main|ai_[a-zA-Z]+)$")
SECRET_PATTERNS = {
    "OpenAI/Anthropic key": re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}"),
    "ElevenLabs key": re.compile(r"\bsk_[a-f0-9]{40,}\b"),
    "Stripe live key": re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{16,}"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),
    "Slack token": re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Telegram bot token": re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b"),
    "Bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._~+/-]{24,}"),
    "JWT": re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    "Private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
NODE_REF_RE = re.compile(r"\$\(\s*'((?:[^'\\]|\\.)+)'\s*\)")
EXPR_RE = re.compile(r"\{\{\s*\$")


def _strings(value):
    """Yield every string inside a nested parameters structure."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v)

SECRET_HEADER_RE = re.compile(r"(api[_-]?key|token|secret|password|authorization|xi-api-key)", re.I)
SAFE_VALUE_RE = re.compile(r"^(=|\{\{|REPLACE|YOUR[_ -]|your[_ -]|<|\$|Bearer\s*\{\{)|^$")


def check_n8n(path: Path) -> tuple[list[str], dict]:
    errors: list[str] = []
    info = {"nodes": 0, "types": 0}
    text = path.read_text(encoding="utf-8")
    try:
        wf = json.loads(text)
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"], info
    nodes = wf.get("nodes")
    conns = wf.get("connections")
    if not isinstance(nodes, list) or not nodes:
        return ["missing or empty `nodes` list"], info
    if not isinstance(conns, dict):
        errors.append("missing `connections` object")
        conns = {}

    names: dict[str, dict] = {}
    types = set()
    for i, n in enumerate(nodes):
        label = n.get("name") or f"#{i}"
        if not n.get("name"):
            errors.append(f"node {label}: missing name")
        elif n["name"] in names:
            errors.append(f"duplicate node name: {n['name']}")
        names[n.get("name", label)] = n
        t = n.get("type")
        if not isinstance(t, str) or not TYPE_RE.match(t):
            errors.append(f"node {label}: bad or missing type {t!r}")
        else:
            types.add(t)
        if not isinstance(n.get("typeVersion"), (int, float)):
            errors.append(f"node {label}: missing numeric typeVersion")
        pos = n.get("position")
        if not (isinstance(pos, list) and len(pos) == 2 and all(isinstance(v, (int, float)) for v in pos)):
            errors.append(f"node {label}: position must be [x, y]")
        if not isinstance(n.get("parameters"), dict):
            errors.append(f"node {label}: parameters must be an object")
        for ctype, cred in (n.get("credentials") or {}).items():
            cid = cred.get("id") if isinstance(cred, dict) else None
            if cid not in PLACEHOLDER_IDS:
                errors.append(f"node {label}: credential {ctype} has a real-looking id {cid!r}; use REPLACE_WITH_YOUR_CREDENTIAL_ID")
        headers = (n.get("parameters") or {}).get("headerParameters", {}).get("parameters", []) or []
        for h in headers:
            name, value = str(h.get("name", "")), h.get("value", "")
            if SECRET_HEADER_RE.search(name) and isinstance(value, str) and not SAFE_VALUE_RE.match(value):
                errors.append(f"node {label}: header {name!r} has a literal value; use a credential or placeholder")

    wired = set()
    for src, outputs in conns.items():
        if src not in names:
            errors.append(f"connection source {src!r} is not a node")
        if not isinstance(outputs, dict):
            errors.append(f"connections[{src!r}] must be an object")
            continue
        for kind, lists in outputs.items():
            if not CONN_KIND_RE.match(kind):
                errors.append(f"connections[{src!r}]: unknown kind {kind!r}")
            for lst in lists or []:
                for c in lst or []:
                    tgt = c.get("node")
                    if tgt not in names:
                        errors.append(f"connection {src!r} -> {tgt!r}: target is not a node")
                    wired.update({src, tgt})
    real = [nm for nm, n in names.items() if not str(n.get("type", "")).endswith(".stickyNote")]
    if len(real) > 1:
        for nm in real:
            if nm not in wired:
                errors.append(f"node {nm!r} is not connected to anything")

    params_text = json.dumps([n.get("parameters", {}) for n in nodes], ensure_ascii=False)
    for n in nodes:
        if str(n.get("type", "")).endswith((".stickyNote", ".code", ".function", ".functionItem")):
            continue
        for s in _strings(n.get("parameters", {})):
            if EXPR_RE.search(s) and not s.startswith("="):
                errors.append(f"node {n.get('name')!r}: text contains {{{{ $... }}}} but is not an expression (missing leading '=')")
                break
    for ref in sorted(set(NODE_REF_RE.findall(params_text))):
        ref = ref.replace("\\'", "'").replace('\\"', '"')
        if ref not in names:
            errors.append(f"expression references unknown node $('{ref}')")

    for label, rx in SECRET_PATTERNS.items():
        m = rx.search(text)
        if m:
            errors.append(f"possible secret ({label}): {m.group(0)[:12]}...")

    md = path.with_suffix(".md")
    if not md.exists():
        errors.append(f"missing companion doc {md.name}")
    elif "source and license" not in md.read_text(encoding="utf-8").lower():
        errors.append(f"{md.name}: needs a 'Source and license' section")

    info = {"nodes": len(real), "types": len(types)}
    return errors, info


def check_activepieces(path: Path) -> list[str]:
    errors = []
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON: {exc}")
    if not path.with_suffix(".md").exists():
        errors.append(f"missing companion doc {path.with_suffix('.md').name}")
    for label, rx in SECRET_PATTERNS.items():
        if rx.search(path.read_text(encoding="utf-8")):
            errors.append(f"possible secret ({label})")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dir", default=str(WF_DIR), help="workflows/ directory")
    args = parser.parse_args()
    base = Path(args.dir).resolve()
    n8n_files = sorted((base / "n8n").rglob("*.json"))
    ap_files = sorted((base / "activepieces").rglob("*.json")) if (base / "activepieces").exists() else []
    if not n8n_files:
        print(f"No n8n workflows found under {base / 'n8n'}")
        return 1

    rows, failures = [], 0
    for f in n8n_files:
        errs, info = check_n8n(f)
        rows.append((f.relative_to(base).as_posix(), info["nodes"], info["types"], "FAIL" if errs else "ok", errs))
    for f in ap_files:
        errs = check_activepieces(f)
        rows.append((f.relative_to(base).as_posix(), "-", "-", "FAIL" if errs else "ok", errs))

    w = max(len(r[0]) for r in rows)
    print(f"{'workflow'.ljust(w)}  nodes  types  status")
    print(f"{'-' * w}  -----  -----  ------")
    for path, nodes, types, status, errs in rows:
        print(f"{path.ljust(w)}  {str(nodes).rjust(5)}  {str(types).rjust(5)}  {status}")
        for e in errs:
            print(f"{' ' * w}    - {e}")
        failures += bool(errs)

    md_orphans = [p for p in (base / "n8n").rglob("*.md") if not p.with_suffix(".json").exists()]
    for p in md_orphans:
        print(f"warning: {p.relative_to(base).as_posix()} has no matching .json")

    total = len(rows)
    if failures:
        print(f"\nFAIL: {failures} of {total} workflow files have problems")
        return 1
    print(f"\nPASS: all {total} workflow files valid ({len(n8n_files)} n8n, {len(ap_files)} Activepieces JSON)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
