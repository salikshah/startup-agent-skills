#!/usr/bin/env python3
"""Validate every skill in skills/ against the Agent Skills spec and this repo's authoring spec.

Checks:
  1. skills/<category>/<skill>/SKILL.md exists.
  2. Frontmatter parses; name and description are present.
  3. name matches the directory, is lowercase-hyphen, 1-64 chars, no consecutive hyphens.
  4. description is 1-1024 chars and contains a trigger phrase.
  5. SKILL.md is under 500 lines.
  6. Required body sections are present in order.
  7. skills/<category>/<skill>/evals/evals.json exists with >= 3 evals.
  8. README skill table reconciles with the skills/ directory.

No third-party dependencies. Exits non-zero with a report if any check fails.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"

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
NAME_RE = re.compile(r"^[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?$")
TRIGGER_WORDS = ("when", "use", "mention", "trigger")


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text: str):
    """Return (data, body). Raises ValueError on malformed frontmatter."""
    if not text.startswith("---"):
        raise ValueError("missing YAML frontmatter (file must start with '---')")
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError("frontmatter block is not closed with a second '---'")

    data: dict = {}
    current_key = None
    for raw in lines[1:end]:
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.lstrip().startswith("- "):
            if current_key is None:
                raise ValueError(f"list item before any key: {line!r}")
            data.setdefault(current_key, []).append(strip_quotes(line.lstrip()[2:].strip()))
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            raise ValueError(f"unparsable frontmatter line: {line!r}")
        key, value = match.group(1), match.group(2).strip()
        if value == "":
            data[key] = []
        else:
            data[key] = strip_quotes(value)
        current_key = key
    return data, "\n".join(lines[end + 1 :])


def skill_dirs():
    return sorted(p.parent for p in SKILLS_DIR.glob("*/*/SKILL.md"))


def validate_skill(skill_dir: Path) -> list[str]:
    errors = []
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    try:
        data, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_dir.relative_to(ROOT)}: {exc}"]

    # name
    fm_name = data.get("name")
    if not isinstance(fm_name, str) or not fm_name.strip():
        errors.append(f"{name}: missing or empty `name` field")
    else:
        if fm_name != name:
            errors.append(f"{name}: name mismatch, directory='{name}' frontmatter='{fm_name}'")
        if not NAME_RE.match(fm_name):
            errors.append(f"{name}: invalid name format '{fm_name}' (lowercase, digits, hyphens only)")
        if "--" in fm_name:
            errors.append(f"{name}: name has consecutive hyphens")

    # description
    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{name}: missing or empty `description` field")
    else:
        if not 1 <= len(description) <= 1024:
            errors.append(f"{name}: description length {len(description)} (must be 1-1024)")
        if not any(word in description.lower() for word in TRIGGER_WORDS):
            errors.append(f"{name}: description lacks trigger phrases ({'/'.join(TRIGGER_WORDS)})")

    # length
    if len(text.splitlines()) > 500:
        errors.append(f"{name}: SKILL.md is {len(text.splitlines())} lines (must be <500)")

    # sections in order
    positions = []
    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^##\s+{re.escape(section)}\s*$", body, re.MULTILINE)
        if not match:
            errors.append(f"{name}: missing required section '## {section}'")
        else:
            positions.append(match.start())
    if positions != sorted(positions):
        errors.append(f"{name}: required sections are out of order")

    # evals
    evals_file = skill_dir / "evals" / "evals.json"
    if not evals_file.exists():
        errors.append(f"{name}: missing evals/evals.json")
    else:
        try:
            evals = json.loads(evals_file.read_text(encoding="utf-8"))
            count = len(evals.get("evals", []))
            if count < 3:
                errors.append(f"{name}: evals.json has {count} evals (must be >=3)")
        except (json.JSONDecodeError, AttributeError) as exc:
            errors.append(f"{name}: evals/evals.json is invalid ({exc})")

    return errors


def validate_readme(actual: set[str]) -> list[str]:
    errors = []
    if not README.exists():
        return [f"missing {README.relative_to(ROOT)}"]
    documented = set()
    row = re.compile(r"^\|[^|]*\|\s*`([a-z0-9-]+)`\s*\|")
    for line in README.read_text(encoding="utf-8").splitlines():
        match = row.match(line)
        if match:
            documented.add(match.group(1))
    undocumented = sorted(actual - documented)
    phantom = sorted(documented - actual)
    if undocumented:
        errors.append("README skill table is missing rows for: " + ", ".join(undocumented))
    if phantom:
        errors.append("README skill table has rows with no skill dir: " + ", ".join(phantom))
    return errors


def main() -> int:
    global SKILLS_DIR
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", default=None, help="path to skills/")
    args = parser.parse_args()
    if args.skills_dir:
        SKILLS_DIR = Path(args.skills_dir).resolve()

    errors = []
    actual = set()
    for skill_dir in skill_dirs():
        actual.add(skill_dir.name)
        errors.extend(validate_skill(skill_dir))
    errors.extend(validate_readme(actual))

    if errors:
        print("Skill validation FAILED:\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"All {len(actual)} skills valid. README table matches skills/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
