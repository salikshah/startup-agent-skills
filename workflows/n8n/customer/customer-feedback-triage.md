# Customer feedback triage: classify, log, route

**Platform:** n8n  |  **Category:** customer  |  **Maps to skill:** lean-startup-method (validated learning), growth-hacking-loop (retention)

Any feedback source -> LLM type/severity/area -> Google Sheet log -> Slack for bugs and churn risk -> Gmail draft reply for churn risks.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Google Sheets, Switch, Slack, If, Gmail

## Credentials

- OpenAI API
- Google Sheets OAuth2
- Slack API
- Gmail OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Sheet tab `feedback`: received_at, source, email, type, severity, area, summary, quote, text.
2. Set both Slack channel ids and your `product_areas`.
3. Point your widget/form webhook at `https://<n8n>/webhook/feedback` with `text` and `email` fields.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/feedback -H 'Content-Type: application/json' -d '{"email":"user@example.com","text":"Export to CSV has been broken for 3 days, we are evaluating other tools."}'
```

## Safety

Replies are drafts only.
