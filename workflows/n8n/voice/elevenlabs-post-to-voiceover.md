# ElevenLabs: post or script to voiceover MP3

**Platform:** n8n  |  **Category:** voice  |  **Maps to skill:** content-strategy-framework (bundle one idea into audio), doing-content-right-sop

Webhook takes post/script text, strips links/hashtags/emoji, calls ElevenLabs TTS and returns an MP3.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, HTTP Request, Respond to Webhook

## Credentials

- Header Auth: name `xi-api-key`, value = your ElevenLabs API key

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Pick a voice in ElevenLabs (Voices > ID) and set `voice_id` in **Config** (default is a premade voice).
2. Activate. Add a Google Drive or S3 node after the TTS node if you want to keep the files.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/voiceover -H 'Content-Type: application/json' -d '{"text":"Shipped: our onboarding is now 3 steps instead of 7. #buildinpublic https://example.com","title":"onboarding"}' --output onboarding.mp3
```

## Safety

Only clone or use voices you have rights to. ElevenLabs bills per character.
