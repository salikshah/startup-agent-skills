# Market monitor: RSS -> LLM relevance -> Telegram digest

**Platform:** n8n  |  **Category:** ops  |  **Maps to skill:** unicorn-pattern-analysis, category-positioning-sop, content-strategy-framework

Polls RSS feeds every 6h, dedupes across runs, keyword/recency prefilter, LLM relevance score + content angle, one Telegram digest.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Schedule, Edit Fields, Code, RSS Read, Remove Duplicates, Limit, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Telegram

## Credentials

- OpenAI API
- Telegram API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Edit `feeds`, `keywords`, `market`. Google News RSS works for any query: `https://news.google.com/rss/search?q=<query>`.
2. Set `telegram_chat_id`. Swap the Telegram node for Slack/email if you prefer.
3. Activate. The first run marks everything as seen and may send a long digest; that's expected.

## How to test

Click *Test workflow* with `min_score` set to 0 to see the full pipeline output.

## Safety

Read-only. LLM cost is capped by the Limit node (25 items per run).
