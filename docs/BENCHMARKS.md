# Benchmarks

Every skill is scored against a fixed 100-point rubric by `tools/benchmark.py`. The rubric is rule-based, so the score is reproducible: two runs on the same tree give the same result. No model, API key, or network is involved.

## Rubric

| Dimension | Points | Checks |
|---|---|---|
| Spec Compliance | 15 | frontmatter parses (5), name valid (3), description has trigger phrases (4), under 500 lines (3) |
| Intent & Triggering | 10 | intent present and non-trivial (5), at least 3 triggers (5) |
| Input/Output Contract | 15 | inputs present (5), outputs present (5), output template or format shown (5) |
| Process Rigor | 20 | at least 5 steps (5), decision points (5), steps sequential (5), edge cases handled (5) |
| Evidence & Sourcing | 10 | evidence section present (5), cites a source (5) |
| Actionability | 15 | examples with numbers (5), checklist or template (5), metrics with targets (5) |
| Measurement | 10 | metrics section present (5), measurable targets (5) |
| Anti-Patterns & Scope | 5 | three or more anti-patterns (5) |

The checks look for content, not style. A check passes when the property is present and the threshold is met. The full scoring logic lives in `tools/benchmark.py`, and each run writes the per-check breakdown to `reports/benchmark.json`.

## Thresholds

| Gate | Requirement | Hard gate |
|---|---|---|
| Spec compliance | 15/15 | yes |
| Overall score | >= 80/100 | yes |
| Evals per skill | >= 3 | yes |
| README reconciliation | exact match with `skills/` | yes |
| Assertion coverage (static evals) | >= 50% | no |
| Assertion pass rate (LLM evals) | >= 80% | no |

The CI workflow runs `tools/validate_skills.py`, `tools/benchmark.py`, and `tools/run_evals.py` (static mode). A push fails if a hard gate fails.

## Reading a score

A skill at 100/100 has every property. A skill at 80/100 meets the ship bar but may lack, for example, a cited source or a target on its metrics. The score measures the document, not whether the skill improves a model's output. Run with `--verbose` to see which checks earned points:

```bash
python tools/benchmark.py --verbose
```

## Why a deterministic rubric

An LLM judge drifts with the model and the prompt. A deterministic rubric does not. The rubric is the gate for merging; the LLM evals (`tools/run_evals.py --llm`) are the second layer, used when a model is available.
