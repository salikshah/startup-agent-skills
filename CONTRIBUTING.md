# Contributing

Thanks for improving Startup Skills. The library covers startup strategy, growth, traction, content, acquisition, planning, and productivity. Contributions should fit that scope and follow the same contract as the existing skills.

## Before you start

- For a new skill, open an issue with the problem it solves, the intended user, and the source material. Wait for a maintainer to confirm scope before writing.
- For fixes, open a pull request directly. Keep it focused on one skill or one tool.
- Do not include client work, personal data, internal codenames, or material you cannot license under MIT.

## Skill contract

Read `SKILL.md` for the full authoring spec. Every skill needs:

- YAML frontmatter with `name`, `description`, `triggers`, and `disable-model-invocation`.
- Eight body sections in order: Intent, Inputs, Process (SOP), Outputs, Evidence, Examples, Metrics, Anti-Patterns.
- At least three evals in `evals/evals.json`.
- Fewer than 500 lines in `SKILL.md`.
- A cited source in Evidence for claims that can be sourced.
- No personal data, credentials, private paths, or unlicensed material.

## Add a skill

1. Create `skills/<category>/<skill-name>/`.
2. Add `SKILL.md` using an existing skill as the template.
3. Add `evals/evals.json` with a happy path, an edge case, and an out-of-scope or deferral case.
4. Add the skill to the table in `README.md`.
5. Run the checks below and fix every failure.
6. Open a pull request.

## Improve a skill

- Keep the change focused. Do not rewrite unrelated sections.
- If behavior changes, update the affected evals.
- If you add a claim that can be sourced, add the source to Evidence.
- Explain the problem and the change in the pull request.

## Evals

- Write prompts a real user would send, including vague or incomplete ones.
- Make each assertion independently checkable. Avoid assertions that restate the whole answer.
- Cover the skill's metrics and anti-patterns where they matter.
- Do not weaken an assertion to make a run pass. Fix the skill instead.

## Checks

```bash
python tools/validate_skills.py
python tools/benchmark.py
python tools/run_evals.py
```

The first two are hard gates. Static evals are a coverage smoke test. LLM mode calls the Anthropic API and costs tokens:

```bash
export ANTHROPIC_API_KEY=...
python tools/run_evals.py --llm --verbose
```

## Pull request checklist

- [ ] The change fits the library's scope.
- [ ] `python tools/validate_skills.py` passes.
- [ ] `python tools/benchmark.py` passes with a score of at least 80.
- [ ] `python tools/run_evals.py` passes.
- [ ] The README table matches `skills/`.
- [ ] No secrets, personal data, or private paths are included.
- [ ] New claims have a source.
- [ ] The pull request explains what changed and why.

## Style

- Write directly and concretely. Prefer a number, a target, or a decision rule over a slogan.
- Avoid hype, guarantees, and invented statistics.
- Present tools and vendors as options, not recommendations. Disclose any relationship you have with a tool you mention.
- Summarize and cite source material. Do not reproduce long passages from books, articles, or paid courses.

## License

By contributing, you agree that your contribution is licensed under the repository's MIT license.
