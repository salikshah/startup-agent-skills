# Job alerts from Greenhouse/Lever/Ashby boards to Telegram

**Platform:** n8n  |  **Category:** ops  |  **Maps to skill:** traction-channel-prioritization (pick targets deliberately), deep-work-protocol (batch the search)

Daily pull of public ATS job boards for chosen companies, filtered by title/location/freshness, visa-sponsorship mentions flagged, deduped across runs, Telegram digest. No LLM, no API keys for the boards.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Schedule, Edit Fields, Code, HTTP Request, Remove Duplicates, Telegram

## Credentials

- Telegram API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Find each company's board id in its careers URL (`boards.greenhouse.io/<id>`, `jobs.lever.co/<id>`, `jobs.ashbyhq.com/<id>`). The ids in **Config** are examples and may change.
2. Edit `title_keywords`, `locations`, `sponsorship_terms`.
3. Set `telegram_chat_id`, activate.

## How to test

Click *Test workflow*; inspect *Normalize and filter* output. Widen `locations` to `[""]` to see everything.

## Safety

Read-only public APIs. The workflow never submits applications.
