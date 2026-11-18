# ElevenLabs post-call webhook to sheet + follow-up Gmail draft

**Platform:** n8n  |  **Category:** voice  |  **Maps to skill:** growth-hacking-loop (activation follow-up), scaling-up-framework

Verifies ElevenLabs post-call HMAC, logs call summary and collected data to Sheets, drafts a follow-up email in Gmail (draft only).

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Webhook, Edit Fields, Code, If, Google Sheets, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Gmail

## Credentials

- Google Sheets OAuth2
- OpenAI API
- Gmail OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. ElevenLabs > Agents settings > Post-call webhook: URL `https://<n8n>/webhook/elevenlabs-post-call`; copy the secret into `webhook_secret`.
2. Allow the crypto module in n8n: env `NODE_FUNCTION_ALLOW_BUILTIN=crypto`.
3. Agent > Analysis > Data collection: add `name`, `email`, `follow_up`.
4. Sheet tab `voice_calls`: date, conversation_id, agent_id, duration_secs, successful, caller_name, caller_email, summary, follow_up.

## How to test

For a dry run set `allow_unsigned` to true, then: curl -X POST http://localhost:5678/webhook-test/elevenlabs-post-call -H 'Content-Type: application/json' -d '{"type":"post_call_transcription","data":{"conversation_id":"c1","agent_id":"a1","analysis":{"transcript_summary":"Caller wants pricing for 10 seats","call_successful":"success","data_collection_results":{"email":{"value":"you@example.com"},"name":{"value":"Sam"}}},"metadata":{"call_duration_secs":95},"transcript":[]}}'. Set it back to false afterwards.

## Safety

Emails are created as Gmail drafts. A human reviews and sends.
