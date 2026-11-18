# Post-eval gate: score a draft, publish only after human approval

**Platform:** n8n  |  **Category:** content  |  **Maps to skill:** post-eval

Scores an X/LinkedIn draft with the repo's post-eval rubric, applies its hard gates, returns the verdict instantly, and asks a human to approve before anything is queued. The X publish node ships disabled.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Respond to Webhook, If, Gmail, Google Sheets, X

## Credentials

- OpenAI API
- Gmail OAuth2 (approval email)
- Google Sheets OAuth2
- X OAuth2 (only if you enable publishing)

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Set `positioning`, `audience`, `approver_email`, `sheet_url` (tab `publish_queue`: approved_at, platform, score, draft, status).
2. Keep `threshold` at 70 to match the skill, or calibrate against your post history.
3. Activate. Leave *Publish to X* disabled unless you have decided approved posts may go out automatically.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/post-eval -H 'Content-Type: application/json' -d '{"platform":"x","draft":"I am building an open-source content engine. Coming soon."}'   # expect DON'T POST, proof capped at 10
```

## Safety

Two gates before publishing: score threshold and an explicit human Approve click. Publishing is off by default.
