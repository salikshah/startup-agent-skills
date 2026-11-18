# Chatwoot resolved conversations to feedback log

**Platform:** n8n  |  **Category:** chatwoot  |  **Maps to skill:** lean-startup-method (validated learning), growth-hacking-loop (retention signals)

On conversation resolved: LLM summary, feedback, bugs and churn risk to a Google Sheet; Slack alert for high churn risk or bugs.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, HTTP Request, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Google Sheets, If, Slack

## Credentials

- Header Auth `api_access_token` (Chatwoot)
- OpenAI API
- Google Sheets OAuth2
- Slack API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Create a sheet tab `support_insights` with headers: date, conversation_id, contact, topic, summary, sentiment, churn_risk, feature_requests, bug_reports, quote.
2. Chatwoot: Settings > Integrations > Webhooks > add `https://<n8n>/webhook/chatwoot-resolved`, event `conversation_status_changed`.
3. Set **Config**, activate.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/chatwoot-resolved -H 'Content-Type: application/json' -d '{"event":"conversation_status_changed","id":1,"status":"resolved","account_id":1}'
```

## Safety

Read-only on Chatwoot. Writes only to your sheet and Slack.
