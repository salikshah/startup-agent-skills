# Chatwoot AI support agent with human handoff

**Platform:** n8n  |  **Category:** chatwoot  |  **Maps to skill:** aeo-geo-playbook (FAQ content), scaling-up-framework (support load)

Answers incoming Chatwoot messages from a knowledge-base file; hands off to a human (holding reply, private note with draft, label, status open, optional team) when confidence is low or the topic is sensitive.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, HTTP Request, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, If

## Credentials

- Header Auth: name `api_access_token`, value = Chatwoot agent-bot token (Settings > Bots) or a user access token
- OpenAI API (or OpenAI-compatible: set the base URL to OpenRouter, Groq or Ollama `http://ollama:11434/v1`)

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Import, open **Config**, set `chatwoot_url`, `company_name`, `kb_url` (a raw markdown/text FAQ).
2. In Chatwoot create an Agent Bot (Settings > Bots) with webhook URL `https://<n8n>/webhook/chatwoot-ai-support`, connect it to an inbox. New conversations then start as `pending` and the bot owns them until handoff.
3. Or, without an agent bot: Settings > Integrations > Webhooks, subscribe to `message_created`, and set `only_when_pending` to false.
4. Activate the workflow.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/chatwoot-ai-support -H 'Content-Type: application/json' -d '{"event":"message_created","message_type":"incoming","private":false,"content":"How do I reset my password?","account":{"id":1},"conversation":{"id":1,"status":"pending","labels":[]},"sender":{"name":"Test"}}'
```

## Safety

The bot never closes or resolves conversations. Refunds, billing, legal and account-access topics always go to a human.
