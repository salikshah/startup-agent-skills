# Recipe: Chatwoot + n8n AI support agent with human handoff

An AI first-line agent inside Chatwoot. It answers from your knowledge base, and when it is unsure, or the topic needs a person, it hands the conversation to your team. Everything is self-hosted on one Docker host.

```
Customer (web widget / WhatsApp / email / Telegram)
        |
     Chatwoot  --(Agent Bot webhook: message_created)-->  n8n workflow
        ^                                                    |
        |   reply, or: holding reply + private note +        |  1. skip if not incoming / private / not pending / labelled
        |   label "ai-handoff" + status "open" (+ team)      |  2. history + knowledge base -> LLM -> {answer, confidence, needs_human}
        +----------------------------------------------------+  3. confident and safe -> reply; otherwise hand off
```

Workflows used:

| File | Role |
|---|---|
| [`n8n/chatwoot/chatwoot-ai-support-agent.json`](../n8n/chatwoot/chatwoot-ai-support-agent.json) | The agent. Knowledge base is a markdown file at a URL. Start here. |
| [`n8n/chatwoot/chatwoot-rag-agent-qdrant.json`](../n8n/chatwoot/chatwoot-rag-agent-qdrant.json) | Same contract, with Qdrant retrieval and Postgres conversation memory. |
| [`n8n/chatwoot/chatwoot-kb-ingest-qdrant.json`](../n8n/chatwoot/chatwoot-kb-ingest-qdrant.json) | Rebuilds the Qdrant knowledge base from Chatwoot Help Center articles. |
| [`n8n/chatwoot/chatwoot-resolved-conversation-insights.json`](../n8n/chatwoot/chatwoot-resolved-conversation-insights.json) | When a conversation is resolved: summary, feedback, churn risk to a sheet + Slack. |

## 1. Run Chatwoot, n8n, Postgres and Redis

Create a folder with these three files.

`docker-compose.yml`:

```yaml
# Chatwoot (rails + sidekiq) + n8n sharing one Postgres (pgvector) and one Redis.
# Based on chatwoot/docker-compose.production.yaml and n8n's Docker docs.
x-chatwoot: &chatwoot
  image: chatwoot/chatwoot:latest
  env_file: .env
  environment:
    - NODE_ENV=production
    - RAILS_ENV=production
    - INSTALLATION_ENV=docker
  volumes:
    - chatwoot_storage:/app/storage
  depends_on: [postgres, redis]
  restart: unless-stopped

services:
  rails:
    <<: *chatwoot
    entrypoint: docker/entrypoints/rails.sh
    command: ["bundle", "exec", "rails", "s", "-p", "3000", "-b", "0.0.0.0"]
    ports: ["127.0.0.1:3000:3000"]

  sidekiq:
    <<: *chatwoot
    command: ["bundle", "exec", "sidekiq", "-C", "config/sidekiq.yml"]

  postgres:
    image: pgvector/pgvector:pg16
    restart: unless-stopped
    environment:
      - POSTGRES_DB=chatwoot
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init:/docker-entrypoint-initdb.d:ro   # creates the n8n database on first start

  redis:
    image: redis:alpine
    restart: unless-stopped
    command: ["sh", "-c", "redis-server --requirepass \"$REDIS_PASSWORD\""]
    env_file: .env
    volumes:
      - redis_data:/data

  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    ports: ["127.0.0.1:5678:5678"]
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_DATABASE=n8n
      - DB_POSTGRESDB_USER=postgres
      - DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}
      - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}
      - WEBHOOK_URL=${N8N_PUBLIC_URL}
      - GENERIC_TIMEZONE=Europe/London
      - NODE_FUNCTION_ALLOW_BUILTIN=crypto   # needed by the ElevenLabs post-call workflow only
      - N8N_DIAGNOSTICS_ENABLED=false
    volumes:
      - n8n_data:/home/node/.n8n
    depends_on: [postgres]

  # Optional, for the RAG variant (same image the n8n starter kit uses)
  qdrant:
    image: qdrant/qdrant
    restart: unless-stopped
    ports: ["127.0.0.1:6333:6333"]
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  chatwoot_storage:
  postgres_data:
  redis_data:
  n8n_data:
  qdrant_data:
```

`init/01-n8n.sql`:

```sql
CREATE DATABASE n8n;
```

`.env` (start from Chatwoot's [`.env.example`](https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example) and make sure these are set):

```bash
SECRET_KEY_BASE=<output of: openssl rand -hex 64>
FRONTEND_URL=http://localhost:3000
POSTGRES_HOST=postgres
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=<strong password>
REDIS_URL=redis://redis:6379
REDIS_PASSWORD=<strong password>
ENABLE_ACCOUNT_SIGNUP=false
N8N_ENCRYPTION_KEY=<output of: openssl rand -hex 32>
N8N_PUBLIC_URL=http://localhost:5678/
```

Start it:

```bash
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
docker compose up -d
curl -I http://localhost:3000/api      # expect 200
```

Open http://localhost:3000 and create the first (admin) account, then http://localhost:5678 for n8n. For anything public, put both behind a reverse proxy with HTTPS (Chatwoot's Docker guide has an Nginx example; keep `underscores_in_headers on;` because the API uses the `api_access_token` header).

If you already run the [n8n self-hosted AI starter kit](https://github.com/n8n-io/self-hosted-ai-starter-kit), skip the `n8n` and `qdrant` services above and attach Chatwoot to the same Docker network instead.

## 2. Set up Chatwoot

1. **Inbox:** *Settings > Inboxes > Add Inbox > Website* (fastest to test). Note the *inbox identifier* on the inbox's *Configuration* tab; the test script needs it.
2. **Knowledge base:** put your FAQ in a markdown file reachable over HTTP (a raw GitHub file, a gist, or a file served by any web server). For the RAG variant, write Help Center articles instead (*Help Center > Portals*) and run `chatwoot-kb-ingest-qdrant`.
3. **Agent Bot:** *Settings > Bots > Add bot* (on older or self-hosted builds without that page: *Super Admin* at `/super_admin` > *Agent Bots*, or `POST /api/v1/accounts/{account_id}/agent_bots` with `name` and `outgoing_url`).
   - Webhook / outgoing URL: `http://n8n:5678/webhook/chatwoot-ai-support` inside this compose network, or your public n8n URL.
   - Copy the bot's **access token**. The workflow uses it to read history and post replies.
4. **Connect the bot to the inbox:** *Settings > Inboxes > (your inbox) > Bot Configuration* > select the bot. New conversations in that inbox now start as **pending**, which means the bot owns them.
5. **Handoff label and team:** create the label `ai-handoff` (*Settings > Labels*). Optionally create a team (*Settings > Teams*) and note its id for `handoff_team_id`.

If you don't want an Agent Bot, use an account webhook instead (*Settings > Integrations > Webhooks*, event `message_created`) with a user access token, and set `only_when_pending` to `false` in the workflow's Config node. The bot then answers in every open conversation until it is labelled `ai-handoff`, so the Agent Bot route is the cleaner one.

## 3. Import and wire the n8n workflow

1. n8n > *Workflows > Import from File* > `workflows/n8n/chatwoot/chatwoot-ai-support-agent.json`.
2. Create credentials:
   - **Header Auth**: name `api_access_token`, value = the Agent Bot token. Select it on every Chatwoot HTTP node (they show a warning until you do).
   - **OpenAI**: an OpenAI key, or point the credential's Base URL at OpenRouter, Groq or Ollama (`http://ollama:11434/v1`) for a local model.
3. Edit **Config**: `chatwoot_url` (`http://rails:3000` inside this compose network, or your public URL), `company_name`, `kb_url`, `confidence_threshold`, `handoff_team_id`.
4. Activate the workflow. The production webhook path is `/webhook/chatwoot-ai-support`.

## 4. The handoff rule

The model returns `{ answer, confidence, needs_human, reason, topic }`. The workflow replies only when **both** hold:

- `confidence >= confidence_threshold` (default 0.75), and
- `needs_human == false`. The prompt forces this to true for refunds, billing disputes, cancellations, legal or privacy requests, account access, and upset customers, and whenever the knowledge base doesn't cover the question.

Otherwise it hands off in this order:

1. Public reply: `handoff_message` ("I'm passing this to a teammate...").
2. Private note with the reason, topic, confidence and the **draft answer that was not sent**, so the agent can reuse it.
3. Label `ai-handoff`. The bot ignores labelled conversations from now on.
4. `toggle_status` to **open**. The conversation leaves the bot's pending queue and shows up for humans.
5. Optional: assign to `handoff_team_id`.

To give a conversation back to the bot, remove the label and set the status back to pending. The bot never resolves or closes conversations.

## 5. Test

**A. Workflow only (no Chatwoot needed):** click *Test workflow* in n8n, then:

```bash
curl -X POST http://localhost:5678/webhook-test/chatwoot-ai-support \
  -H 'Content-Type: application/json' \
  -d '{"event":"message_created","message_type":"incoming","private":false,
       "content":"How do I reset my password?",
       "account":{"id":1},"conversation":{"id":1,"status":"pending","labels":[]},
       "sender":{"name":"Test"}}'
```

The Chatwoot HTTP calls fail if conversation 1 doesn't exist, but you can inspect the LLM decision in the execution.

**B. End to end through Chatwoot's public Client API** (website inbox):

```bash
#!/usr/bin/env bash
set -euo pipefail
CW=http://localhost:3000
INBOX=<inbox identifier from the inbox Configuration tab>
ACCOUNT=1
TOKEN=<a user access token, Profile settings>   # only used to read the result

# 1) create a contact
CONTACT=$(curl -s -X POST "$CW/public/api/v1/inboxes/$INBOX/contacts" \
  -H 'Content-Type: application/json' -d '{"name":"Recipe Test","email":"recipe-test@example.com"}')
CID=$(echo "$CONTACT" | python3 -c 'import sys,json;print(json.load(sys.stdin)["source_id"])')

# 2) open a conversation and send a question the FAQ answers
CONV=$(curl -s -X POST "$CW/public/api/v1/inboxes/$INBOX/contacts/$CID/conversations" -H 'Content-Type: application/json' -d '{}')
CONV_ID=$(echo "$CONV" | python3 -c 'import sys,json;print(json.load(sys.stdin)["id"])')
curl -s -X POST "$CW/public/api/v1/inboxes/$INBOX/contacts/$CID/conversations/$CONV_ID/messages" \
  -H 'Content-Type: application/json' -d '{"content":"How do I reset my password?"}' > /dev/null

# 3) and one that must be handed off
curl -s -X POST "$CW/public/api/v1/inboxes/$INBOX/contacts/$CID/conversations/$CONV_ID/messages" \
  -H 'Content-Type: application/json' -d '{"content":"I want a refund for last month, this is unacceptable."}' > /dev/null

sleep 15
# 4) read back: expect an AI answer, then the holding reply + a private note, label ai-handoff, status open
curl -s "$CW/api/v1/accounts/$ACCOUNT/conversations/$CONV_ID/messages" -H "api_access_token: $TOKEN" \
  | python3 -c 'import sys,json;[print(m["message_type"], m.get("private"), (m.get("content") or "")[:90]) for m in json.load(sys.stdin)["payload"]]'
curl -s "$CW/api/v1/accounts/$ACCOUNT/conversations/$CONV_ID" -H "api_access_token: $TOKEN" \
  | python3 -c 'import sys,json;c=json.load(sys.stdin);print("status:",c["status"],"labels:",c.get("labels"))'
```

Pass criteria: the first question gets an answer drawn from your FAQ. The refund message produces the holding reply, a private note, the `ai-handoff` label and status `open`. After that the bot stays silent in this conversation.

## 6. WhatsApp (optional)

- **Official route (recommended for production):** add a WhatsApp inbox in Chatwoot using the WhatsApp Cloud API. The bot works unchanged because it only sees Chatwoot events.
- **Evolution API route:** [Evolution API](https://github.com/EvolutionAPI/evolution-api) has a built-in Chatwoot integration. Create an instance, then call `POST /chatwoot/set/{instance}` with your Chatwoot `url`, `accountId`, a user `token`, `nameInbox`, and `conversationPending: true` (so new chats start pending and the bot picks them up). Evolution creates the inbox and relays messages both ways, so no n8n bridge is needed. Template [6544](https://n8n.io/workflows/6544) and [6988](https://n8n.io/workflows/6988) by thiagovazzoler show an n8n-based bridge if you need custom media handling. Evolution's Baileys mode uses the unofficial WhatsApp Web protocol, which can get numbers banned. Use it for testing, not for customer traffic you can't afford to lose.

## 7. RAG variant

1. Write Help Center articles, run `chatwoot-kb-ingest-qdrant` once (or let it run weekly). It clears and rebuilds the `support_kb` collection.
2. Import `chatwoot-rag-agent-qdrant.json`, add Qdrant (`http://qdrant:6333`, no key locally) and Postgres credentials (host `postgres`, database `n8n` or a separate one).
3. Point the Agent Bot at `/webhook/chatwoot-rag-agent` instead.
4. Use the same embedding model in both workflows. To run fully local, swap the OpenAI chat/embedding nodes for *Ollama Chat Model* / *Embeddings Ollama* (the starter kit pulls `llama3.2`).

## 8. Activepieces variant

See [activepieces/chatwoot/chatwoot-ai-support.md](../activepieces/chatwoot/chatwoot-ai-support.md). In short: *Chatwoot > New Incoming Message* (or *Webhook* registered as the Agent Bot URL) -> *Code* (skip rules) -> *HTTP* history + FAQ -> *AI > Extract Structured Data* (`answer`, `confidence`, `needs_human`, `reason`) -> *Router* -> *Chatwoot > Send Message*, or the same four handoff HTTP calls.

## Troubleshooting

- **The bot replies to itself:** check that *Should the bot answer?* sees `message_type: "incoming"`. Outgoing bot messages also fire `message_created`.
- **401 from Chatwoot:** the Header Auth name must be exactly `api_access_token`, and a reverse proxy must pass headers that contain underscores.
- **Nothing happens:** the inbox has no bot connected, or the conversation isn't `pending`. Set `only_when_pending` to false to test with account webhooks.
- **Chatwoot rejects the internal webhook URL:** use n8n's public HTTPS URL (`WEBHOOK_URL`).
