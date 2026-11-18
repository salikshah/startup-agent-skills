# ElevenLabs: Telegram voice note to tasks

**Platform:** n8n  |  **Category:** voice  |  **Maps to skill:** deep-work-protocol (capture without context switching), ai-native-build-log

Telegram voice note -> ElevenLabs Scribe transcript -> LLM task extraction -> Google Sheet rows + Telegram confirmation.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Telegram Trigger, Edit Fields, If, Telegram, HTTP Request, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Code, Google Sheets

## Credentials

- Telegram API (bot token from @BotFather)
- Header Auth `xi-api-key` (ElevenLabs)
- OpenAI API
- Google Sheets OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Create a sheet tab `tasks` with headers: created_at, title, due_date, priority, context, status.
2. Message your bot once, read your chat id from the trigger output, put it in `allowed_chat_id`.
3. Activate (Telegram triggers need a public HTTPS n8n URL; use `WEBHOOK_URL` or a tunnel). Swap the Sheets node for Todoist/Notion if you prefer.

## How to test

Activate, send the bot a 10-second voice note: "Tomorrow email Sam the pilot proposal, and on Friday review the metrics deck." Expect two rows and a reply.

## Safety

Ignores every chat except yours. Nothing is sent to third parties beyond ElevenLabs and your LLM.
