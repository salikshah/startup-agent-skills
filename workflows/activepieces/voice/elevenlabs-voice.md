# ElevenLabs voice flows (Activepieces)

**Platform:** Activepieces  |  **Category:** voice  |  **Maps to skill:** content-strategy-framework, deep-work-protocol  |  **n8n equivalent:** `n8n/voice/elevenlabs-post-to-voiceover.json, elevenlabs-dictation-to-tasks.json, elevenlabs-agent-tools-webhook.json`

Three flows: post to voiceover, voice note to tasks, and a webhook backend for ElevenLabs agent tools.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- ElevenLabs (*Text to Speech*)
- OpenAI (*Transcribe*) or HTTP to ElevenLabs speech-to-text
- Telegram Bot (*New Message*, *Get File*, *Send Text Message*)
- AI (*Extract Structured Data*)
- Google Sheets (*Insert Row*)
- Webhook (*Catch Webhook*, *Return Response*)
- Router

## Steps

1. **Post to voiceover.** *Webhook > Catch Webhook* (text) -> *Code* (strip links, hashtags, emoji; reject over 4,500 chars) -> *ElevenLabs > Text to Speech* (voice, model `eleven_multilingual_v2`) -> *Webhook > Return Response* with the file, or save it with *Google Drive > Upload File*.
2. **Voice note to tasks.** *Telegram Bot > New Message* -> *Router* (only your chat id and only messages with `voice`) -> *Telegram Bot > Get File* -> *HTTP* POST multipart to `https://api.elevenlabs.io/v1/speech-to-text` (`file`, `model_id=scribe_v1`, header `xi-api-key`); the ElevenLabs piece has no speech-to-text action, so use HTTP or *OpenAI > Transcribe* -> *AI > Extract Structured Data* (list of tasks with title, due date, priority) -> *Loop on Items* -> *Google Sheets > Insert Row* -> *Telegram Bot > Send Text Message* with the summary.
3. **Agent server tools.** *Webhook > Catch Webhook* -> *Code* (compare header `x-tool-secret` with a value kept in a project variable/connection; route on `?tool=`) -> *Router*: `lookup_faq` -> *HTTP* get FAQ -> *AI > Ask AI* (two spoken sentences) -> *Return Response*; `capture_lead` -> *Google Sheets > Insert Row* -> *Return Response*; else *Return Response* 401.
4. In ElevenLabs, add each tool as a Webhook tool pointing at the Activepieces webhook URL (use the `/sync` variant so the agent waits for the response).

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Create a Speech-to-Text API with OpenAI GPT-4o-mini Transcribe](https://cloud.activepieces.com/templates/6EoGKTWkx4LX5lkaGuqKm) (`6EoGKTWkx4LX5lkaGuqKm`)

## Notes

The ElevenLabs piece also manages agents, knowledge-base documents and tools, which is handy for syncing your FAQ into the agent's own knowledge base.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
