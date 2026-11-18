# Chatwoot RAG agent (Qdrant + Postgres memory) with handoff

**Platform:** n8n  |  **Category:** chatwoot  |  **Maps to skill:** aeo-geo-playbook, scaling-up-framework

AI Agent answers Chatwoot messages using a Qdrant knowledge-base tool and per-conversation Postgres memory; same handoff path as the basic agent.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, AI Agent, OpenAI Chat Model, Postgres Memory, Qdrant, OpenAI Embeddings, Structured Output Parser, If, HTTP Request

## Credentials

- Header Auth `api_access_token` (Chatwoot)
- OpenAI API (chat + embeddings) or swap for Ollama nodes
- Qdrant API (starter kit: URL `http://qdrant:6333`, no key)
- Postgres (starter kit: host `postgres`, values from `.env`)

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Run `chatwoot-kb-ingest-qdrant` first so the `support_kb` collection exists. Use the same embedding model in both workflows.
2. Set **Config** and connect a Chatwoot Agent Bot to `https://<n8n>/webhook/chatwoot-rag-agent`.
3. Activate.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/chatwoot-rag-agent -H 'Content-Type: application/json' -d '{"event":"message_created","message_type":"incoming","private":false,"content":"Do you have a free plan?","account":{"id":1},"conversation":{"id":1,"status":"pending","labels":[]}}'
```

## Safety

Same as the basic agent: no auto-resolve, sensitive topics always handed off.
