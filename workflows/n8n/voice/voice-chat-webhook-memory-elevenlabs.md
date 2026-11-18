# AI voice chat using webhook, memory manager, OpenAI, Gemini and ElevenLabs

**Platform:** n8n  |  **Category:** voice  |  **Maps to skill:** ai-native-build-log

Receives a recorded voice message on a webhook, transcribes it with OpenAI, keeps chat memory, answers with Gemini and returns ElevenLabs speech.

## Source and license

- Original author: Ayoub (ayoub-n8n)
- Original source: https://n8n.io/workflows/2405
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Memory Manager, Aggregate, Window Memory, Gemini Chat Model, Respond to Webhook, HTTP Request, Limit, Basic LLM Chain, Webhook, OpenAI

## Credentials

- OpenAI API (transcription)
- Google Gemini (PaLM) API
- Header/Custom Auth for ElevenLabs `xi-api-key`

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Set the ElevenLabs voice id in the HTTP node URL.
2. Wire your front end (browser recorder or Shortcuts) to POST the audio file to the webhook `voice_message`.

## How to test

Activate, then POST an audio file as multipart field to `/webhook/voice_message` and play the returned audio.
