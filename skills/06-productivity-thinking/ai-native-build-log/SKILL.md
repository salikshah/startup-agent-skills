---
name: ai-native-build-log
description: Document and demonstrate how to build software with AI-native workflows — prompting, agent orchestration, build process, and the result. Use when the user mentions an AI-native build, building with AI, an AI-native workflow, prompting process, agent orchestration, or a build log.
triggers:
  - "AI-native build"
  - "how I built with AI"
  - "AI-native workflow"
  - "prompting process"
  - "agent orchestration"
  - "build log"
disable-model-invocation: false
---

# AI-Native Build Log

## Intent
Document the process of building software with AI-native workflows, including the method and the result. It shows founders, collaborators, and clients that you build with AI and can prove it.

## Inputs
- A specific feature, repo, or prototype you built
- The prompts you used (or sanitized versions)
- The agents/tools involved (coding agents, model providers, orchestration)
- Iteration count and time spent
- Final output and metrics

## Process (SOP)

1. Define the build target in one sentence: what, for whom, and what "done" means.
2. Map the AI-native stack: coding agent, models, orchestration, and tools.
3. Write the prompt before the code, with role, context, task, constraints, and output format.
4. Run the orchestration loop and record every agent handoff and human gate.
5. Iterate against evals until the build passes, then record the metrics.
6. Publish the build log with sanitized prompts, edits, and results.

If the build is not reproducible, treat it as a demo and say so. When to stop: stop prompting and fix the spec when three iterations produce the same failure.

### Step 1: Define the Build Target
Write a one-sentence spec. What are you building? For whom? What does "done" look like? Example: "A force-controlled sanding simulation in MuJoCo with an admittance force loop at 5N."

### Step 2: Map the AI-Native Stack
List every AI tool in the workflow:
- Coding agent (e.g., Claude Code, Cursor, Codex)
- Model providers (Anthropic, OpenAI, Gemini, local llama.cpp)
- Orchestration (LangGraph, CrewAI, or custom)
- Tools (web crawlers, analytics libraries, etc.)

### Step 3: Prompt-First Development
Write the prompt before the code. Structure it:
- Role: "You are an expert MuJoCo roboticist."
- Context: "Building a force-controlled sanding simulation."
- Task: "Generate the MJCF model, the admittance control loop, and the runner."
- Constraints: "Pure Python, deterministic, <200 lines per file."
- Output format: "Code blocks only, no explanation."

### Step 4: Agent Orchestration Loop
If using multi-agent:
- Orchestrator agent decomposes the task into subtasks
- Worker agents execute in parallel (coding, testing, docs)
- Review agent validates output against spec
- Human approves or rejects at each gate

### Step 5: Iterate with Evals
Run the build. Measure:
- Time to first working output
- Lines of code written by AI vs human
- Number of iterations to pass tests
- Test pass rate

### Step 6: Document the Log
Write it up as a public build log:
- What you prompted
- What the AI produced
- What you edited
- Why you edited it (the human judgment layer)
- Time saved vs traditional build

## Outputs
- A public build log (markdown or blog post)
- A "how I built with AI" case study
- Reusable prompt templates for similar builds
- Metrics: time saved, iteration count, AI/human code ratio

## Evidence
Source: the build-log format synthesizes reproducible engineering write-ups: target, stack, prompts, iterations, human edits, and measured result. A log without prompts or metrics is a story, not evidence.

## Examples
**Build log entry:** "Spent 4 hours prompting a coding agent to generate a physics model. 12 iterations to get the contact model right. Human edited 30% of the code (contact stiffness parameters). Time saved: ~12 hours vs traditional build."

## Metrics
- Time to first working output. Target: under 1 day for a scoped feature.
- AI/human code ratio. Target: report the ratio, not a vanity number.
- Iteration count to pass tests. Target: under 10.
- Build log published. Target: within 48 hours of the build.

## Anti-Patterns
- Claiming AI-native without actually using AI in the build
- Hiding the human judgment layer (editing, architecture decisions) to inflate the AI contribution
- Skipping the eval step — no metrics means no proof
- Using vague prompts ("build a robot") instead of structured, specific prompts
