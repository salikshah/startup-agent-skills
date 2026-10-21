# Framework comparison

How this repo compares with open-source skill libraries aimed at similar users. The comparison covers process and scope, not prose quality. Counts and CI facts were checked on 21 October 2026 from each repo's README and `.github/workflows`; they change, so re-check before citing.

Libraries compared:

- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills): 52 marketing skills. Mature distribution through npx, Claude Code and Codex plugins, and per-skill ZIPs. Ships per-skill evals, frontmatter validation, and regression tests in CI. Runs a disclosed partner program.
- [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills): 78 marketing skills. npm installer. CI validates frontmatter and the README table.
- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills): 398 multi-domain skills, 766 standard-library Python tools, and converters for 13 agent platforms. CI includes a Tessl quality review with a 70/100 merge threshold, a security audit, and a broad quality gate.

## Feature matrix

| Capability | This repo | coreyhaines31 | OpenClaudia | alirezarezvani |
|---|---|---|---|---|
| Skills | 14 | 52 | 78 | 398 |
| Folder + `SKILL.md` layout | yes | yes | yes | yes |
| Frontmatter validation in CI | yes | yes | yes | yes |
| Required body sections enforced | yes | no | no | partial |
| Per-skill prompt evals | yes | yes | no | not verified |
| Eval runner in CI | yes (static) | no | no | no |
| Skill quality score | yes (fixed 100-point rubric) | no | no | yes (Tessl, 70 threshold) |
| CI on pull requests | yes | yes | yes | yes |
| Installer or multi-agent packaging | no | yes | yes | yes |
| Authoring standard | yes | partial (CONTRIBUTING) | partial (CONTRIBUTING) | yes |
| License | MIT | MIT | MIT | MIT |

## Where this repo leads

- **Reproducible scoring.** Among the compared repos, this is the only one with an in-repo, rule-based 100-point rubric that runs offline and fails the build below 80. alirezarezvani uses an external Tessl review with a 70 threshold; coreyhaines31 and OpenClaudia validate structure.
- **Eval runner.** This repo ships per-skill prompt evals and `tools/run_evals.py`, which runs them in CI in static mode. coreyhaines31 ships evals but no eval runner in CI. OpenClaudia ships no prompt evals; alirezarezvani documents a quality review but no per-skill prompt evals.
- **Body contract.** The validator enforces eight named sections in order. The compared repos do not publish a fixed eight-section body contract.
- **Auditability.** Fourteen skills, one authoring spec, and one benchmark fit in a single review pass.

## Where this repo is smaller

- **Volume.** 14 skills against 52, 78, and 398. Coverage of adjacent tasks is thinner.
- **Distribution.** No npm package, plugin marketplace listing, platform converters, or ZIP releases. Installation is clone-and-copy.
- **Tooling.** No bundled CLIs, Python tools, reference trees, or API integrations. The larger libraries ship hundreds.
- **Track record.** No public users, stars, forks, or outside contributions yet.

## Eval caveat

The benchmark scores the document. It does not test model behavior. A 100/100 means every required property appears; it does not prove the skill improves output. Static evals measure term coverage, and LLM evals are single-arm and judge-graded. Dedicated harnesses cover this gap: [agent-skills-eval](https://github.com/darkrishabh/agent-skills-eval) compares with-skill and without-skill runs, and [skillcheck](https://github.com/sx4im/skillcheck) adds blind A/B grading and bootstrap confidence intervals. Treat this repo's scores as a merge gate, not a behavioral benchmark.

## The tradeoff

A large library wins on coverage and installation. This repo wins on a single auditable contract per skill. The gap is narrower than the skill counts suggest: coreyhaines31 already runs CI and ships evals, and alirezarezvani gates skill quality with Tessl. The remaining edge is reproducibility and the required body contract.
