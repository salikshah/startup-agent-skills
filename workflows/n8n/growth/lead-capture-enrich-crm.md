# Lead capture: enrich, score ICP fit, upsert sheet CRM, alert Slack

**Platform:** n8n  |  **Category:** growth  |  **Maps to skill:** traction-channel-prioritization, growth-hacking-loop, category-positioning-sop (ICP)

Form webhook -> spam/validity filter -> homepage fetch -> LLM enrichment and ICP score -> upsert on email in a Google Sheet CRM -> Slack alert for strong fits.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, If, HTTP Request, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Google Sheets, Slack

## Credentials

- OpenAI API
- Google Sheets OAuth2
- Slack API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Sheet tab `leads` with headers: email, name, company, website, message, source, summary, industry, size, icp_fit, intent, next_step, updated_at.
2. Point your site form (Webflow, Framer, Tally webhook, plain HTML) at `https://<n8n>/webhook/lead`. Add a hidden `company_website_confirm` field as a honeypot.
3. Edit `icp` and `fit_threshold`. Swap the Sheets node for HubSpot/Pipedrive nodes if you have a CRM.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/lead -H 'Content-Type: application/json' -d '{"email":"cto@n8n.io","name":"Test CTO","company":"n8n","message":"Want a demo for 30 engineers"}'
```

## Safety

No outreach is triggered. Personal data goes only to your sheet, Slack and LLM provider; mention this in your privacy notice.
