# Support FAQ chat widget (n8n Chat + Qdrant RAG)

**Platform:** n8n  |  **Category:** customer  |  **Maps to skill:** aeo-geo-playbook (answer-ready content)

Embeddable public chat that answers from a Qdrant FAQ collection and declines when the KB has no answer.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Chat Trigger, AI Agent, OpenAI Chat Model, Window Memory, Qdrant, OpenAI Embeddings

## Credentials

- OpenAI API (or Ollama chat/embeddings)
- Qdrant API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Build the `support_kb` collection first (see `chatwoot-kb-ingest-qdrant`, or load your own docs with the same embedding model).
2. Replace support@example.com in the agent system message.
3. Activate; copy the chat URL or embed with `@n8n/chat` on your site.

## How to test

Open the chat URL shown on the Chat node and ask a question that is, and one that is not, in your KB.

## Safety

Public endpoint: set a usage cap on your LLM key and consider n8n's basic auth option on the Chat node.
