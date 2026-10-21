---
name: post-eval
description: Evaluate a draft social post (X/Twitter or LinkedIn) before publishing. Scores strategic alignment, proof of work, content quality, timing, and risk, then recommends POST or DON'T POST. Use when the user says "evaluate this post", "should I post this", "review my tweet", "check this LinkedIn", "is this post good", or pastes draft copy for feedback.
triggers:
  - "evaluate this post"
  - "should I post this"
  - "review my tweet"
  - "check this LinkedIn"
  - "is this post good"
  - "post feedback"
disable-model-invocation: false
---

# Post Evaluation Skill

## Intent
Evaluate a draft post before publishing. Score it against the author's strategic goals, proof of work, content quality, timing, and risk, then recommend POST or DON'T POST with specific reasoning and fixes.

## Inputs
- The draft post text
- Platform (X/Twitter or LinkedIn)
- The author's current positioning and target audience (if provided)
- Any proof assets the post could link to (repo, case study, audit, article)

## Process (SOP)

1. Read the draft and confirm the platform, audience, positioning, and available proof assets.
2. Score strategic alignment, proof of work, content quality, timing, and risk using the rubric below.
3. Check the risk gates: promises, confidentiality, and misinterpretation.
4. Decide POST or DON'T POST against the 70-point threshold.
5. Write the verdict, gaps, and one specific rewrite or next action.

If the draft has no link, artefact, or result, cap the proof-of-work score at 10/25 and recommend a concrete asset to publish first. If the platform is unclear, ask before scoring. When to stop: do not score a draft the author has not written; evaluate only supplied copy.

### Score dimensions

#### 1. Strategic Alignment (20 points)
- Does it advance the author's stated positioning or area of expertise?
- Does it demonstrate expertise or only announce intent?
- Does it have a clear CTA?
- Does it target the intended audience?

#### 2. Proof of Work (25 points)
- Does it link to something concrete (repo, audit, case study, article)?
- Does it show results or only describe them?
- Is there evidence the author can actually do what they claim?

#### 3. Content Quality (20 points)
- Is the hook strong enough to stop the scroll?
- Is the value proposition clear in 2 sentences?
- Is the tone authentic (not corporate, not AI-sounding)?
- Is it concise (X: <=280 chars, LinkedIn: <=1500 chars)?

#### 4. Timing & Context (15 points)
- Is there a reason to post NOW vs later?
- Does it ride a current trend or news cycle?
- Is the target audience active at this time?

#### 5. Risk Assessment (20 points)
- Could this post attract negative attention?
- Does it reveal too much about unlaunched work?
- Does it make promises the author can't keep?
- Could it be misinterpreted?

## Outputs

### VERDICT: POST or DON'T POST

**Score:** [X]/100

**Pros:**
- [Bullet points]

**Cons:**
- [Bullet points]

**Strategic Analysis:**
- [2-3 sentences on how this advances or hurts the author's goals]

**Gaps:**
- [What's missing that would make this post stronger]

**Recommendation:**
- [Specific action: post now, wait for X, rewrite Y, or don't post]

**If POST:**
- Best time to post: [day/time in the author's timezone]
- Hashtags: [relevant hashtags]
- Engagement hook: [question or CTA to add]

**If DON'T POST:**
- What to do instead: [specific alternative]
- When to post: [what needs to happen first]

**Pre-flight checklist:**
- [ ] The post links to a real artefact or result
- [ ] The hook survives a two-second skim
- [ ] The CTA is explicit
- [ ] The claims match the evidence
- [ ] The platform and timing are deliberate

## Evidence
Source: the rubric synthesizes standard pre-publish review criteria — strategic alignment, proof of work, content quality, timing, and risk — normalized to 100 points with a 70-point POST threshold. The weights are a starting point; calibrate them against your own post history.

## Examples
**Draft:** "I'm building an open-source content engine. Coming soon."
**Verdict:** DON'T POST (48/100). No artefact, no number, no CTA. Announces intent instead of demonstrating work.
**Fix:** Publish a short case study of something already shipped, with a link and one measurable result, then post that.

## Metrics
- Verdict calibration: fraction of POST recommendations that hold up after publishing. Target: 70%+.
- Score distribution across evaluated drafts. Target: fewer than 20% of drafts below 50/100 after revision.
- Time from draft to decision. Target: under 10 minutes.

## Anti-Patterns
- Posting "I'm building" without showing what was built
- Posting the same content on X and LinkedIn without adaptation
- Posting without a CTA
- Posting when there is nothing to link to
- Posting too frequently without substance
- Posting about AI without demonstrating AI expertise
- Treating the score as a substitute for audience judgment
