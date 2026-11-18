# Repurpose one post or article into an X thread + LinkedIn post

**Platform:** n8n  |  **Category:** content  |  **Maps to skill:** content-strategy-framework, doing-content-right-sop, post-eval (next step)

Text or URL in; X thread, LinkedIn post and 3 alternative hooks out, with per-tweet length checks; drafts logged to Sheets, nothing published.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, If, HTTP Request, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Google Sheets, Respond to Webhook

## Credentials

- OpenAI API
- Google Sheets OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Sheet tab `content_queue`: created_at, source, x_thread, linkedin_post, warnings, status.
2. Edit `voice` in **Config** to match yours.
3. Activate.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/repurpose -H 'Content-Type: application/json' -d '{"text":"We cut onboarding from 7 steps to 3 and activation went from 22% to 41% in two weeks. Here is what we removed and why..."}'
```

## Safety

Drafts only. Pair with post-eval-gate before anything goes out.
