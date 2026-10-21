<p align="center">
  <img src="Startup%20Agent%20Skills%20by%20Salik%20Shah%20v2.png" alt="Startup Agent Skills by Salik Shah" width="100%">
</p>

<h1 align="center">Startup Agent Skills</h1>

<p align="center">
  <a href="https://agentskills.io/specification.md"><img src="https://img.shields.io/badge/spec-agentskills.io-blue.svg" alt="Agent Skills Spec"></a>
  <a href=".github/workflows/validate-skills.yml"><img src="https://img.shields.io/badge/CI-passing-success.svg" alt="CI Validation"></a>
  <a href="docs/BENCHMARKS.md"><img src="https://img.shields.io/badge/benchmark-100%25%20pass%20rate-brightgreen.svg" alt="Benchmark Score"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-informational.svg" alt="License: MIT"></a>
  <a href="https://salikshah.com"><img src="https://img.shields.io/badge/web-salikshah.com-4F46E5?style=flat&logo=googlechrome&logoColor=white" alt="Website"></a>
  <a href="https://x.com/salik"><img src="https://img.shields.io/badge/𝕏-@salik-000000?style=flat&logo=x&logoColor=white" alt="X / Twitter"></a>
  <a href="https://linkedin.com/in/salikshah"><img src="https://img.shields.io/badge/LinkedIn-SalikShah-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

<p align="center">
  <strong>Executable, benchmarked Agent Skills for startup strategy, growth, and positioning.</strong><br>
  CI-gated for Antigravity, Codex, Claude Code, Cursor, Opencode, Hermes &amp; others.
</p>

Fourteen executable, CI-gated skills that turn AI coding agents into strategic startup operators. Built on the [Agent Skills specification](https://agentskills.io/specification.md), each skill is a structured SOP distilled from the canonical startup literature (Eric Ries, Gabriel Weinberg, Sean Ellis, Cal Newport, Bharat Anand).

Compatible with **Antigravity**, **Codex**, **Claude Code**, **Cursor**, **Opencode**, **Hermes**, and any autonomous agent runtime.

---

## Why Startup Agent Skills?

Most AI agent instructions are unvalidated prompts: they lack boundaries, drift over time, and provide no testable proof that they work. 

**Startup Skills** takes an engineering approach to startup operating procedures:
- **Strict Input/Output Contracts:** Every skill specifies required inputs, step-by-step SOPs, concrete outputs, and edge cases.
- **Rooted in Proven Canon:** No synthetic hype. Every tactic references primary sources with real-world examples and metrics.
- **Deterministic 100-Point Benchmark:** Every skill is scored offline by `tools/benchmark.py` against an 8-dimension rubric (`docs/BENCHMARKS.md`).
- **Test Evals Included:** Ships with `evals.json` test suites and a test runner (`tools/run_evals.py`) supporting both zero-dependency static coverage and LLM judge modes.

---

## Skills Directory

| Category | Skill | What it does | Source / Canon |
|---|---|---|---|
| 00-post-eval | `post-eval` | Score a draft X/LinkedIn post against strategic proof of work and decide whether to publish | Pre-publish review rubric |
| 01-startup-strategy | `lean-startup-method` | Run the Build-Measure-Learn loop and choose pivot or persevere | *The Lean Startup* (Eric Ries) |
| 02-growth-traction | `growth-hacking-loop` | Find and scale the highest-leverage growth channel with rapid tests | *Hacking Growth* (Sean Ellis) |
| 02-growth-traction | `traction-channel-prioritization` | Rank the 19 traction channels with the bullseye framework | *Traction* (Gabriel Weinberg) |
| 02-growth-traction | `aeo-geo-playbook` | Build an AI-visibility system for answer engines (ChatGPT, Perplexity, Claude) | Generative Engine Optimization |
| 03-scaling-leadership | `scaling-up-framework` | Align people, strategy, execution, and cash to scale past founder-led stage | *Scaling Up* (Verne Harnish) |
| 04-content-marketing | `content-strategy-framework` | Build a bundled, linked content strategy that avoids the content trap | *The Content Trap* (Bharat Anand) |
| 04-content-marketing | `doing-content-right-sop` | Build a sustainable, distribution-first content engine | *Doing Content Right* (Steph Smith) |
| 05-exit-acquisition | `acquisition-readiness-audit` | Prepare a company for acquisition and organize due diligence | *Getting Acquired* (Andrew Gazdecki) |
| 06-productivity-thinking | `deep-work-protocol` | Design rituals and schedules for distraction-free deep work | *Deep Work* (Cal Newport) |
| 06-productivity-thinking | `ai-native-build-log` | Document the AI-native build process as proof of work | AI Engineering Canon |
| 07-case-studies | `unicorn-pattern-analysis` | Extract repeatable category and timing patterns across unicorn startups | Unicorn Pattern Matrix |
| 08-planning-process | `business-plan-template` | Write an investor-ready business plan with bottom-up sizing | *How to Write a Winning Business Plan* (Walter Grant) |
| 08-planning-process | `category-positioning-sop` | Turn a thin AI wrapper into a defensible category leader | Category Design Principles |

---

## Quickstart & Installation

### Option A: Install All Skills in Claude Code / Antigravity
```bash
git clone https://github.com/SalikShah/startup-agent-skills.git
cp -r startup-agent-skills/skills/* ~/.claude/skills/
```

### Option B: Use in Cursor
Copy any `SKILL.md` file directly into your project's `.cursor/rules/` directory or reference it in `.cursorrules`.

### Option C: Try the Offline Web App
Open [`post-eval-app/index.html`](post-eval-app/index.html) directly in any browser. It is a zero-dependency, local-first interactive evaluator for testing social drafts before publishing.

---

## Anatomy of a Skill

Each skill lives at `skills/<category>/<skill-name>/SKILL.md` and implements the required 8-section contract:

```markdown
---
name: skill-name
description: What it does, when to use it, and trigger phrases.
triggers:
  - "trigger phrase 1"
  - "trigger phrase 2"
disable-model-invocation: false
---

# Skill Name

## Intent
What this skill does and the exact scenarios where it should trigger.

## Inputs
Information required before execution (data, metrics, stage).

## Process (SOP)
Sequential, numbered steps with explicit decision gates and edge cases.

## Outputs
Concrete deliverables produced (checklists, matrices, decision logs).

## Evidence
Foundational citation or methodology principles.

## Examples
Real-world application showing concrete figures and trade-offs.

## Metrics
Quantifiable targets to verify if execution succeeded.

## Anti-Patterns
Common failure modes, false shortcuts, and anti-patterns to avoid.
```

---

## Verification & Evals

Every skill in this repo is continuously verified by automated tooling:

```bash
# 1. Spec & frontmatter compliance (hard gate)
python tools/validate_skills.py

# 2. Score against the 100-point quality rubric (hard gate, min 80)
python tools/benchmark.py

# 3. Run prompt evals (static coverage by default; pass --llm for API grading)
python tools/run_evals.py
```

See [docs/EVAL_FRAMEWORK.md](docs/EVAL_FRAMEWORK.md) for eval mechanics and [docs/FRAMEWORK_COMPARISON.md](docs/FRAMEWORK_COMPARISON.md) for a direct comparison with other open-source skill libraries.

---

## Contributing

Contributions are welcome. Please ensure:
1. Every new skill adheres strictly to the 8-section contract in [SKILL.md](SKILL.md).
2. `skills/<category>/<skill-name>/evals/evals.json` contains at least 3 distinct evals.
3. `python tools/validate_skills.py` and `python tools/benchmark.py` pass with scores $\ge 80$.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

[MIT](LICENSE) © 2026 Salik Shah
