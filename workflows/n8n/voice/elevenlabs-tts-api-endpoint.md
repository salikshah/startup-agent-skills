# Generate text-to-speech using ElevenLabs via API

**Platform:** n8n  |  **Category:** voice  |  **Maps to skill:** content-strategy-framework

Webhook endpoint: POST text + voice id, returns ElevenLabs audio; validates input with an IF node.

## Source and license

- Original author: Emmanuel Bernard (n8ninja)
- Original source: https://n8n.io/workflows/2245
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `Generate Text-to-Speech Using Elevenlabs via API.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

If, Respond to Webhook, Webhook, HTTP Request

## Credentials

- Custom Auth / Header Auth with header `xi-api-key` (see the sticky note in the workflow)

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Create the ElevenLabs credential, open the HTTP node and select it.
2. Activate and POST `{"voice_id":"...","text":"..."}`.

## How to test

`webhook-test/` URLs work while the editor is listening (click *Test workflow* first). After activation use `webhook/`.

```bash
curl -X POST http://localhost:5678/webhook-test/generate-voice -H 'Content-Type: application/json' -d '{"voice_id":"21m00Tcm4TlvDq8ikWAM","text":"Hello from n8n"}' --output hello.mp3
```
