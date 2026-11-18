# ElevenLabs voice agent: n8n server tools

**Platform:** n8n  |  **Category:** voice  |  **Maps to skill:** traction-channel-prioritization (voice as a channel), growth-hacking-loop

Webhook backend for ElevenLabs Conversational AI server tools: `lookup_faq` (knowledge-base answer in two spoken sentences) and `capture_lead` (append to Sheets), with shared-secret header check.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, Switch, HTTP Request, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Respond to Webhook, Google Sheets

## Credentials

- OpenAI API
- Google Sheets OAuth2
- (none for ElevenLabs: it calls you; you check `x-tool-secret`)

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Set `shared_secret` to a long random string, plus `kb_url` and `sheet_url` (tab `voice_leads`: created_at, name, email, phone, interest, conversation_id).
2. ElevenLabs > Agents > your agent > Tools > Add tool > Webhook. Tool 1 `lookup_faq`: POST `https://<n8n>/webhook/elevenlabs-tools?tool=lookup_faq`, header `x-tool-secret`, body param `question` (string, "the caller's question").
3. Tool 2 `capture_lead`: same URL with `?tool=capture_lead`, body params `name`, `email`, `phone`, `interest`.
4. In the agent prompt say when to call each tool. Activate the workflow.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST 'http://localhost:5678/webhook-test/elevenlabs-tools?tool=lookup_faq' -H 'Content-Type: application/json' -H 'x-tool-secret: <your secret>' -d '{"question":"What are your opening hours?"}'
```

## Safety

Requests without the secret get 401. The agent cannot send email or take payments through these tools.
