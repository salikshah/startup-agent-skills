# Eval framework

An eval is a test for a skill. It has three parts: a prompt a user might send, the output a correct response must contain, and assertions a grader can check.

## Format

Each skill ships `skills/<category>/<skill>/evals/evals.json`:

```json
{
  "skill_name": "lean-startup-method",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic user request",
      "expected_output": "What a correct response must contain or do",
      "assertions": [
        "Specific, checkable requirement",
        "A second requirement"
      ],
      "files": []
    }
  ]
}
```

- `prompt` — a request a user might type. Cover the happy path, an edge case, and an out-of-scope case.
- `expected_output` — the shape of a correct answer, written as prose.
- `assertions` — atomic, checkable requirements. Each one should be verifiable on its own.
- `files` — optional fixture paths the eval depends on.

Write at least 3 evals per skill. The validator enforces this.

## Running evals

```bash
python tools/run_evals.py              # static mode, no network
python tools/run_evals.py --llm        # LLM-judge mode, needs ANTHROPIC_API_KEY
python tools/run_evals.py --verbose    # per-eval breakdown
```

The runner writes `reports/evals.json`. In LLM mode, set `ANTHROPIC_MODEL` or pass `--model` to choose the model (default: `claude-sonnet-4-5`).

### Static mode

Static mode checks coverage, not correctness. For each assertion, it extracts significant terms (lowercase words of 4+ characters, stopwords removed) and counts the assertion as covered when a third or more of those terms appear in the skill's `SKILL.md` and `references/`. It is a smoke test: it confirms the skill talks about what the eval asks for.

Static mode needs no network and no key. It is the default because it always runs.

### LLM mode

LLM mode runs two calls per eval. First it sends the skill's instructions and the eval prompt to Claude to produce an agent response. Then it sends that response, the expected output, and the assertions to a judge call, which marks each assertion passed or failed. It measures whether the skill, read as written, produces the expected behavior. Pass rate threshold is 80%.

LLM mode needs `ANTHROPIC_API_KEY`. It is slower and costs tokens, so it runs on demand, not in CI.

## Adding an eval

1. Open the skill's `evals/evals.json`.
2. Add an object with `id`, `prompt`, `expected_output`, `assertions`, `files`.
3. Run `python tools/run_evals.py` and confirm coverage.
4. Run `python tools/validate_skills.py` and confirm the count is still >= 3.

## Coverage versus correctness

Static coverage and LLM pass rate answer different questions. Coverage asks whether the skill contains the concepts. Pass rate asks whether the skill produces the behavior. A skill can score high on coverage and low on pass rate when the concepts are present but the instructions are weak. Treat pass rate as the stronger signal.
