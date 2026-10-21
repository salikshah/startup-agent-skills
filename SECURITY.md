# Security policy

## Supported versions

Security fixes target the `main` branch. There is no formal backport window for older tags.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting on this repository: open the **Security** tab and choose **Report a vulnerability**. If private reporting is unavailable, open a minimal issue asking for a private channel. Do not include exploit details, credentials, or personal data in a public issue.

Include:

- The affected file, skill, or workflow.
- The commit or version where you reproduced it.
- Steps to reproduce, with the smallest useful example.
- The impact you believe it has.
- A suggested fix, if you have one.

You will get a best-effort response. There is no paid bug bounty and no guaranteed response time.

## Scope

In scope:

- Python tools in `tools/`.
- The CI workflow in `.github/workflows/`.
- The local demo at `post-eval-app/index.html`.
- Skill instructions that could cause data exfiltration, destructive commands, credential access, prompt injection, or unsafe tool use.
- Secrets committed to the repository.

Out of scope:

- Vulnerabilities in third-party agents or runtimes that load these skills.
- Social engineering, spam, or physical attacks.
- Reports that require access to another person's data or systems.

## Safe harbor

Good-faith research is welcome. Do not access other people's data, disrupt services, or test against systems you do not own. Limit testing to a local copy of this repository.

## Secrets

Never commit API keys, tokens, or credentials. The tools read `ANTHROPIC_API_KEY` from the environment when LLM eval mode is requested. If a key is exposed, revoke and rotate it first, then report the exposure.

## Skill risk

Skills are instructions, not sandboxed code. Review a skill before running it, especially if it includes scripts or asks an agent to run commands. The Python tools make no network calls in static mode; LLM eval mode is opt-in and sends prompts to the Anthropic API.
