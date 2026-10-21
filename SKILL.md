# Skill Authoring Spec

This document defines the format every skill in this repository must follow. The validator (`tools/validate_skills.py`) enforces it.

## File layout

```
skills/<category>/<skill-name>/
├── SKILL.md            # required
├── evals/
│   └── evals.json      # required
├── references/         # optional — move detail here if SKILL.md is long
├── scripts/            # optional
└── assets/             # optional
```

## Frontmatter

The first bytes of `SKILL.md` must be a YAML block delimited by `---`:

```yaml
---
name: skill-name
description: One to three sentences: what it does, when to use it, and trigger phrases.
triggers:
  - "trigger phrase 1"
  - "trigger phrase 2"
disable-model-invocation: false
---
```

Rules (from the Agent Skills spec):

- `name` — 1–64 chars, lowercase `a-z`, digits, and hyphens only. No consecutive hyphens. Must match the directory name.
- `description` — 1–1024 chars. Must state when to use the skill and include trigger phrases.
- `triggers` — list of user phrases that should invoke the skill.
- `disable-model-invocation` — boolean. `true` means only humans invoke it; `false` (default) means the model may auto-invoke.

## Body sections

Every skill must contain these sections, in this order:

1. **Intent** — what it does and when to use it.
2. **Inputs** — what information is needed to execute it.
3. **Process (SOP)** — numbered steps. Include decision points, sequencing, and edge cases.
4. **Outputs** — what it produces.
5. **Evidence** — the source and the concepts it rests on (book, chapter, or first principles).
6. **Examples** — a real-world application with concrete numbers.
7. **Metrics** — how to measure whether it worked, with targets where possible.
8. **Anti-Patterns** — what NOT to do.

## Constraints

- `SKILL.md` must be under **500 lines**. Move detail to `references/`.
- No personal data: no real names, emails, phone numbers, client lists, internal codenames, or private paths.
- Claims that can be sourced must cite their source in **Evidence**.
- Avoid overclaiming. Say "typically", "target", or "healthy range" rather than "always" or "never" unless the source supports it.

## Evals

Each skill ships `evals/evals.json`:

```json
{
  "skill_name": "skill-name",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic user request",
      "expected_output": "What a correct response must contain or do",
      "assertions": [
        "Specific, checkable requirement",
        "..."
      ],
      "files": []
    }
  ]
}
```

Guidelines:

- At least **3 evals per skill**: a happy path, an edge case, and an out-of-scope / deferral case.
- `assertions` must be specific and checkable, not vague.
- Cover the skill's stated metrics and anti-patterns.

## Benchmarks

Every skill is scored against a 100-point rubric. Ship threshold: **>= 80**. Spec compliance is a hard gate. See `docs/BENCHMARKS.md`.
