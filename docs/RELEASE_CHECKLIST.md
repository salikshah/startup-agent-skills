# Release checklist

One page, used for every public release. Do not skip a box because the previous release passed.

## 1. Freeze

- [ ] Choose the version. Use `v1.0.0` for the first public release.
- [ ] Confirm the scope and the README table match `skills/`.
- [ ] Run the private release scan from the maintainer notes. Do not commit the scan list.
- [ ] Confirm every source is cited and no long copyrighted passages were added.

## 2. Clean

- [ ] Remove `reports/`, `tools/__pycache__/`, and all `*.pyc` files.
- [ ] Confirm `.gitignore` covers generated output.
- [ ] Confirm `post-eval-app/index.html` still works offline and makes no network calls.

## 3. Verify

- [ ] `python tools/validate_skills.py` passes.
- [ ] `python tools/benchmark.py` passes with every skill at 80 or above.
- [ ] `python tools/run_evals.py` passes.
- [ ] Optional: run one LLM eval with `--llm` and record the token cost.
- [ ] CI is green on the release commit.
- [ ] `docs/FRAMEWORK_COMPARISON.md` facts are still current. Update the checked date if they are not.

## 4. Package

- [ ] Initialize git if this is the first release.
- [ ] Stage files and confirm `reports/`, `__pycache__/`, and `*.pyc` are absent from `git status`.
- [ ] Commit with a message that states the version and scope.
- [ ] Tag the commit, for example `v1.0.0`.
- [ ] If shipping a ZIP, exclude `.git/`, `reports/`, `__pycache__/`, and `*.pyc`.

## 5. Publish

- [ ] Get explicit maintainer approval before pushing, creating a public repository, or publishing a release.
- [ ] Push the commit and tag to the approved remote.
- [ ] Enable private vulnerability reporting.
- [ ] Protect the default branch and require the CI check.
- [ ] Confirm CI passes on the published commit.

## 6. After

- [ ] Announce with the version, scope, and install steps.
- [ ] Watch issues and security reports for the first week.
- [ ] Record known limitations. LLM eval mode is optional and is not part of CI.
- [ ] Set a date for the next review.
