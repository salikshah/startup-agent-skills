---
name: aeo-geo-playbook
description: Answer Engine Optimization / Generative Engine Optimization playbook. A repeatable system for becoming the answer AI engines give for your category queries. Use when the user mentions AEO, GEO, AI visibility, answer engine optimization, generative engine optimization, or getting cited by ChatGPT, Claude, Perplexity, Gemini, or Google AI Overviews.
triggers:
  - "AEO playbook"
  - "GEO playbook"
  - "AI visibility audit"
  - "answer engine optimization"
  - "generative engine optimization"
disable-model-invocation: false
---

# AEO/GEO Playbook

## Intent
Build a repeatable AI-visibility system. Any startup can use this to become the answer ChatGPT, Claude, Perplexity, Gemini, and Google AI Overviews give for its category queries.

## Inputs
- Target company name and website
- Top 10 queries in its category
- Top 5 competitors
- Current AI visibility baseline (screenshots + data)

## Process (SOP)

1. Audit the baseline: query 50 category prompts across the target engines and record mentions, citations, and competitors.
2. Map every query to a content module and design the pillar-cluster, llms.txt, schema, and semantic HTML.
3. Produce 14 content modules: long-form articles, short answers, case studies, and teardowns.
4. Distribute: publish the modules, implement llms.txt and JSON-LD, add internal links, and allow AI crawlers.
5. Measure weekly and refresh the modules that do not earn citations.

If an engine blocks crawling, fix robots.txt and server access before producing more content. When to stop: if mention rate does not move after 8 weeks, audit query fit and citation sources before scaling production.

### Phase 1: Baseline Audit (Week 1)
Query each AI engine with 50 target queries. Record:
- Is the brand mentioned? (Y/N)
- Which competitor is cited instead?
- What sources are cited?
- Screenshots + timestamps + raw responses

Output: `baseline-audit.md` with raw data + gap analysis.

### Phase 2: Content Engine Blueprint (Week 2)
Map every query to a content module. Design:
- Pillar-cluster architecture (topic clusters with internal linking)
- llms.txt (structured index for AI agents)
- JSON-LD schema (Organization, WebSite, Article, FAQ)
- Semantic HTML (proper heading hierarchy, code examples, tables)

Output: `content-engine-blueprint.md`

### Phase 3: Production (Weeks 3-4)
Produce 14 content modules:
- 5 long-form articles (2,000–5,000 words, structured for AI citation)
- 5 short-form answers (200–500 words, direct answers to specific queries)
- 2 case studies (proof of work, citation-ready structure)
- 2 competitive teardowns (structured for citation)

Output: Published content with full schema.

### Phase 4: Distribution (Week 5)
- Implement llms.txt
- Add JSON-LD schema to all pages
- Optimize semantic HTML
- Build internal linking web (3-5 internal links per article)
- Submit to AI crawlers (allow GPTBot, ClaudeBot, PerplexityBot)

Output: Live pages with technical optimization.

### Phase 5: Measurement (Week 6+)
Weekly tracking:
- AI mention rate per engine (target: high share for category queries)
- Citation count (who cites you, for what)
- Traffic from AI sources (Google Analytics)
- Conversion from AI traffic

Monthly:
- Traffic from AI sources (track trend)
- Conversion from AI traffic (track trend)

Output: `measurement-dashboard.md`

## Outputs
- Baseline audit report
- Content engine blueprint
- 10 published content modules
- llms.txt + JSON-LD + semantic HTML
- Measurement dashboard with 6 weeks of data

**Pre-flight checklist:**
- [ ] 50 baseline queries captured with screenshots
- [ ] Every query mapped to a module
- [ ] llms.txt and JSON-LD validated
- [ ] AI crawlers allowed
- [ ] Weekly measurement scheduled

## Evidence
AEO/GEO emerged as a distinct discipline as answer engines began citing sources directly. The mechanics differ from SEO: the optimization target is citation, not keyword rank, so content must be structured for machine consumption (llms.txt, schema, clear answer framing).

## Examples
**Query:** "What's the best AI customer support platform?"
**Before:** Brand mentioned in 0/5 engines.
**After:** Brand mentioned in 5/5 engines, cited as a top answer in 4/5.

## Metrics
- AI mention rate (weekly per engine). Target: 30%+ of priority queries by week 12.
- Citation count (domains citing you). Target: 10+ distinct domains by week 12.
- Traffic from AI sources (monthly). Target: 20% month-over-month growth.
- Conversion from AI traffic (monthly). Target: 2%+.

## Anti-Patterns
- Optimizing for keyword rank instead of citation
- Skipping llms.txt (AI agents read it before crawling page content)
- Skipping measurement (no data means no proof of impact)
- Treating AEO as SEO with a new name (the mechanics differ: citation, not rank)
