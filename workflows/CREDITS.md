# Credits

Every source used for `workflows/`, with author, URL and license. *Original* means written for this repository and released under the repo's MIT license. *Adapted* means copied from a licensed source with the changes listed.

## Adapted n8n workflows

All of these were copied from [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates), which is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (Copyright (c) 2024-2026 Enes Cingoz). Most entries in that collection mirror community templates first published on n8n.io; the original creator is credited below. Changes in every file: credential IDs replaced with `REPLACE_WITH_YOUR_CREDENTIAL_ID`, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.

| Workflow in this repo | Original author | Original source | Status |
|---|---|---|---|
| `n8n/voice/elevenlabs-tts-api-endpoint.json` | Emmanuel Bernard (n8ninja) | https://n8n.io/workflows/2245 | adapted |
| `n8n/voice/voice-chat-webhook-memory-elevenlabs.json` | Ayoub (ayoub-n8n) | https://n8n.io/workflows/2405 | adapted |
| `n8n/voice/voice-rag-agent-elevenlabs-qdrant.json` | Davide Boizza (n3witalia) | https://n8n.io/workflows/2846 | adapted |
| `n8n/content/article-to-thread-and-linkedin.json` | contributor not named (added to enescingoz/awesome-n8n-templates on 2026-07-15) | https://github.com/enescingoz/awesome-n8n-templates (`Grounded Article to Thread and LinkedIn Post.json`) | adapted |
| `n8n/growth/qualify-leads-sheets-openai.json` | Yulia (yulia) | https://n8n.io/workflows/2163 | adapted |
| `n8n/growth/website-grounded-cold-email-writer.json` | contributor not named (added to enescingoz/awesome-n8n-templates on 2026-07-15) | https://github.com/enescingoz/awesome-n8n-templates (`Website-Grounded Cold Email Writer.json`) | adapted |
| `n8n/customer/feedback-sentiment-form-to-sheets.json` | MilanWR (milanwr) | https://n8n.io/workflows/1996 | adapted |
| `n8n/customer/slack-support-channel-to-linear-tickets.json` | Jimleuk (jimleuk) | https://n8n.io/workflows/2323 | adapted |
| `n8n/customer/summarize-form-feedback-report.json` | Yulia (yulia) | https://n8n.io/workflows/2164 | adapted |
| `n8n/ops/hn-who-is-hiring-scraper.json` | Julian Kaiser (jksr) | https://n8n.io/workflows/2924 | adapted |

## Original workflows and guides (MIT, Salik Shah)

- `n8n/chatwoot/chatwoot-ai-support-agent.json`
- `n8n/chatwoot/chatwoot-rag-agent-qdrant.json`
- `n8n/chatwoot/chatwoot-kb-ingest-qdrant.json`
- `n8n/chatwoot/chatwoot-resolved-conversation-insights.json`
- `n8n/voice/elevenlabs-post-to-voiceover.json`
- `n8n/voice/elevenlabs-dictation-to-tasks.json`
- `n8n/voice/elevenlabs-agent-tools-webhook.json`
- `n8n/voice/elevenlabs-post-call-to-crm.json`
- `n8n/content/post-eval-gate.json`
- `n8n/content/content-repurpose-post-to-threads.json`
- `n8n/growth/lead-capture-enrich-crm.json`
- `n8n/growth/cold-outreach-gmail-drafts.json`
- `n8n/customer/customer-feedback-triage.json`
- `n8n/customer/support-faq-rag-chat.json`
- `n8n/ops/weekly-metrics-digest.json`
- `n8n/ops/market-rss-monitor.json`
- `n8n/ops/job-opportunity-alerts.json`
- `activepieces/chatwoot/chatwoot-ai-support.md`
- `activepieces/voice/elevenlabs-voice.md`
- `activepieces/content/post-eval-gate.md`
- `activepieces/content/content-repurpose.md`
- `activepieces/growth/lead-capture-enrich.md`
- `activepieces/growth/cold-outreach-drafts.md`
- `activepieces/customer/feedback-triage.md`
- `activepieces/customer/support-faq.md`
- `activepieces/ops/weekly-metrics-digest.md`
- `activepieces/ops/market-rss-monitor.md`
- `activepieces/ops/job-alerts.md`

Some originals were informed by public templates (read for API shapes and ideas, not copied):

- *Build a multichannel customer support AI assistant with Chatwoot & OpenRouter* by zrgrn, https://n8n.io/workflows/8260 (Chatwoot webhook/message API usage).
- *Route Chatwoot customer chats to AI and live agents with Groq and Gemini* by mohanlaldhanwani, https://n8n.io/workflows/16039 (AI-to-human routing idea).
- *Forward Chatwoot messages to WhatsApp via Evolution API* by thiagovazzoler, https://n8n.io/workflows/6544, and *WhatsApp to Chatwoot message forwarder*, https://n8n.io/workflows/6988 (WhatsApp bridge; the recipe uses Evolution API's built-in Chatwoot integration instead).
- *Book Cal.com meetings from ElevenLabs voice agent conversations* by automation-wizard, https://n8n.io/workflows/5665 (ElevenLabs server-tool webhook pattern).
- *Draft and approve LinkedIn posts from RSS news* by postwire, https://n8n.io/workflows/20649 (Gmail send-and-wait approval shape).
- *Write compliant cold email drafts in Gmail* by gabeao, https://n8n.io/workflows/21243 (Gmail draft node shape).

## Activepieces

- [activepieces/activepieces](https://github.com/activepieces/activepieces), MIT for the community edition. Piece and action names in the guides were checked against `packages/pieces/` on 2026-11-18.
- Official template gallery: https://cloud.activepieces.com/templates (public API `https://cloud.activepieces.com/api/v1/templates`, 420 templates on 2026-11-18). The guides **link** to templates by ID and do not copy their JSON, because the gallery states no license for template content (and some templates are ports of n8n templates).

## Infrastructure and references

- [n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit), Apache-2.0: Docker Compose for n8n + Postgres + Qdrant + Ollama. Linked from the quickstart and recipe; service names follow it.
- [devlikeapro/n8n-nodes-chatwoot](https://github.com/devlikeapro/n8n-nodes-chatwoot), MIT: optional Chatwoot community node, mentioned in the recipe. The workflows use plain HTTP Request nodes so no community node is required.
- [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp), MIT: its node database was used offline to check that every node type and typeVersion in these workflows exists.
- [Chatwoot](https://github.com/chatwoot/chatwoot) (MIT, with enterprise features under a separate license) docs: https://developers.chatwoot.com. [ElevenLabs](https://elevenlabs.io/docs) API docs. [Evolution API](https://github.com/EvolutionAPI/evolution-api) (Apache-2.0 based).

## Considered and not used

- [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) (MIT, 2,061 JSON files at commit 94007c1): 1,363 of the 2,061 files have connections pointing at nodes that are not in the file (node IDs instead of names, plus generated `error-handler-*` targets), and only 1 file still contains any LangChain/AI node. They would not import as working workflows, so none were vendored.
- [wassupjay/n8n-free-templates](https://github.com/wassupjay/n8n-free-templates): no license file, so it cannot be redistributed.
- n8n.io template library (https://api.n8n.io/api/templates): templates carry no license field, so JSON was only copied where a licensed collection redistributes it (above).
- Two Automatia BCN "Lite" templates from the enescingoz collection (FlowScribe Lite, SupportFlow Lite) were dropped because they use `n8n-nodes-base.openAi` typeVersion 1.8, which does not exist (latest is 1.1).
