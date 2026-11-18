# Chatwoot Help Center to Qdrant knowledge base

**Platform:** n8n  |  **Category:** chatwoot  |  **Maps to skill:** aeo-geo-playbook (one source of truth for answers)

Rebuilds a Qdrant collection from published Chatwoot Help Center articles (weekly or on demand).

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Manual, Schedule, Edit Fields, HTTP Request, Code, Qdrant, OpenAI Embeddings, Document Loader, Text Splitter

## Credentials

- Header Auth `api_access_token` (Chatwoot user token with Help Center access)
- OpenAI API (embeddings) or Ollama embeddings
- Qdrant API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Create a Help Center portal in Chatwoot and publish a few articles.
2. Set `account_id`, `portal_slug`, `qdrant_url` in **Config**.
3. Click *Test workflow*; check Qdrant at `http://localhost:6333/dashboard`.

## How to test

Run manually in the editor; then query `curl http://localhost:6333/collections/support_kb` and expect `points_count` > 0.

## Safety

Clearing the collection is intentional (full rebuild). Point it at a dedicated collection.
