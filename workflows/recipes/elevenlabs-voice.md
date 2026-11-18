# Recipe: ElevenLabs voice workflows with n8n

Three voice patterns for a small team, plus the post-call loop:

| Pattern | Workflow | What you get |
|---|---|---|
| Dictation -> agent -> tasks | [`n8n/voice/elevenlabs-dictation-to-tasks.json`](../n8n/voice/elevenlabs-dictation-to-tasks.json) | Talk to a Telegram bot. Tasks land in a sheet and the bot confirms them. |
| Post -> voiceover | [`n8n/voice/elevenlabs-post-to-voiceover.json`](../n8n/voice/elevenlabs-post-to-voiceover.json) | POST a post, script or newsletter and get an MP3 back for a podcast, video VO or audio version. |
| Voice agent calling n8n tools | [`n8n/voice/elevenlabs-agent-tools-webhook.json`](../n8n/voice/elevenlabs-agent-tools-webhook.json) | An ElevenLabs phone/web agent that answers from your FAQ and captures leads through n8n. |
| After the call | [`n8n/voice/elevenlabs-post-call-to-crm.json`](../n8n/voice/elevenlabs-post-call-to-crm.json) | HMAC-verified post-call webhook: call log in Sheets plus a follow-up email as a Gmail draft. |

Related adapted workflows: [`voice-rag-agent-elevenlabs-qdrant`](../n8n/voice/voice-rag-agent-elevenlabs-qdrant.md) (agent tool backed by Qdrant RAG, by Davide Boizza), [`voice-chat-webhook-memory-elevenlabs`](../n8n/voice/voice-chat-webhook-memory-elevenlabs.md) (browser voice chat with memory, by Ayoub), [`elevenlabs-tts-api-endpoint`](../n8n/voice/elevenlabs-tts-api-endpoint.md) (minimal TTS API, by Emmanuel Bernard).

## 0. One-time setup

1. ElevenLabs > *Developers > API Keys*: create a key. Restrict it to the scopes you need (text to speech, speech to text) if your plan allows.
2. n8n > *Credentials > New > Header Auth*: name `xi-api-key`, value = the key. All ElevenLabs HTTP nodes use this credential, and the key never appears in workflow JSON.
3. Pick a voice: *Voices* > copy the voice ID. The workflows default to a premade voice (`21m00Tcm4TlvDq8ikWAM`); change it in **Config**.
4. Public HTTPS for n8n (`WEBHOOK_URL`). Telegram and ElevenLabs must be able to reach your webhooks.

Costs: text to speech bills per character, speech to text per audio minute, agents per call minute. The voiceover workflow refuses text over `max_chars` (4,500) so one bad request can't burn your quota.

## 1. Dictation -> agent -> tasks

```
Telegram voice note -> (only your chat id) -> download file -> ElevenLabs Scribe (speech-to-text, model scribe_v1)
   -> LLM: tasks[{title, due_date, priority, context}] + summary
   -> Google Sheet "tasks" (one row per task)   and   Telegram reply "Captured 2 task(s): ..."
```

1. Create a bot with @BotFather and add the token as a *Telegram API* credential.
2. Import the workflow. Sheet tab `tasks`: created_at, title, due_date, priority, context, status.
3. Send the bot any message, open the execution, copy `message.chat.id` into `allowed_chat_id`. Every other chat is ignored.
4. Set `timezone` so "tomorrow" and "Friday" resolve correctly. Activate.

Test: send a voice note, for example: "Tomorrow send Priya the pilot proposal. Friday, review the weekly metrics. Someday, look at Activepieces." Expect three rows, with due dates on the first two, and a reply listing them.

To make it an agent rather than a capture tool, replace the *Extract tasks* chain with an AI Agent node that has tools (Google Calendar, Todoist, Gmail *draft*, Notion). Keep the chat-id allow-list.

## 2. Post -> voiceover

```
POST /webhook/voiceover {text, voice_id?, title?} -> strip links/hashtags/emoji/markdown -> ElevenLabs TTS -> MP3 response
```

```bash
curl -X POST https://<n8n>/webhook/voiceover \
  -H 'Content-Type: application/json' \
  -d '{"title":"onboarding-update","text":"We cut onboarding from seven steps to three. Activation went from 22 to 41 percent in two weeks. Here is what we removed."}' \
  --output onboarding-update.mp3
```

Tips:

- Write numbers the way they should be spoken ("22 percent") or add a pronunciation dictionary in ElevenLabs.
- For a two-host podcast, have an LLM write the script as alternating lines, call TTS once per line with two voice IDs, and join the files with ffmpeg (an *Execute Command* node on self-hosted n8n).
- To publish the audio, add *Google Drive > Upload* or *S3* after the TTS node. Don't post the audio automatically; run the text through [`post-eval-gate`](../n8n/content/post-eval-gate.md) first.

## 3. Voice agent calling n8n tools

```
Caller <-> ElevenLabs Agent --(server tool: POST + x-tool-secret)--> n8n /webhook/elevenlabs-tools?tool=...
                                                                      |-- lookup_faq  -> FAQ text -> LLM -> {answer, found}
                                                                      |-- capture_lead -> Google Sheet "voice_leads" -> {ok}
                                                                      |-- no/bad secret -> 401
```

1. Import `elevenlabs-agent-tools-webhook.json`. In **Config** set `shared_secret` to a long random string (`openssl rand -hex 24`), plus `kb_url` and `sheet_url`. Activate.
2. ElevenLabs > *Agents* > create an agent. Its system prompt should include rules like:
   > You are the receptionist for Acme. For any question about the product, prices, hours or policies, call `lookup_faq` with the caller's question and read back the answer. If the caller wants a follow-up, collect name, email, phone and what they need, confirm them, then call `capture_lead`. Never make up information.
3. *Tools > Add tool > Webhook*, twice:

   | Tool name | Method / URL | Headers | Body parameters |
   |---|---|---|---|
   | `lookup_faq` | POST `https://<n8n>/webhook/elevenlabs-tools?tool=lookup_faq` | `x-tool-secret: <shared_secret>` (store it as a workspace secret) | `question` (string, required): "The caller's question in their words" |
   | `capture_lead` | POST `https://<n8n>/webhook/elevenlabs-tools?tool=capture_lead` | same | `name`, `email`, `phone`, `interest` (strings) |

4. Test the tools directly, then from the agent's *Test AI agent* button:

```bash
curl -X POST 'https://<n8n>/webhook/elevenlabs-tools?tool=lookup_faq' \
  -H 'Content-Type: application/json' -H 'x-tool-secret: <shared_secret>' \
  -d '{"question":"Do you have a free plan?"}'
# -> {"answer":"...","found":true}

curl -X POST 'https://<n8n>/webhook/elevenlabs-tools?tool=lookup_faq' -H 'Content-Type: application/json' -d '{}'
# -> 401 {"error":"unauthorized"}
```

Keep tool answers short. The agent reads them aloud, so two sentences beat a paragraph. The `lookup_faq` prompt enforces that limit.

For a larger knowledge base, use the adapted [`voice-rag-agent-elevenlabs-qdrant`](../n8n/voice/voice-rag-agent-elevenlabs-qdrant.md), or upload your docs to the agent's own ElevenLabs knowledge base and keep n8n for actions only.

## 4. After the call: post-call webhook

1. ElevenLabs > *Agents* > settings > *Post-call webhook*: URL `https://<n8n>/webhook/elevenlabs-post-call`. Copy the webhook secret into `webhook_secret` in **Config**.
2. n8n container env: `NODE_FUNCTION_ALLOW_BUILTIN=crypto` (the Code node verifies the `elevenlabs-signature` HMAC over the raw body and rejects stale timestamps).
3. Agent > *Analysis > Data collection*: add `name`, `email` and `follow_up` so the webhook carries them.
4. Sheet tab `voice_calls`: date, conversation_id, agent_id, duration_secs, successful, caller_name, caller_email, summary, follow_up.

Each verified call becomes a row. If the caller left an email, an LLM writes a follow-up and it is saved as a **Gmail draft** for you to check and send. The workflow has no send step.

## Activepieces variant

See [activepieces/voice/elevenlabs-voice.md](../activepieces/voice/elevenlabs-voice.md). The ElevenLabs piece covers *Text to Speech* and agent/knowledge-base management. It has no speech-to-text action, so use *HTTP* to `https://api.elevenlabs.io/v1/speech-to-text` or *OpenAI > Transcribe*. For agent tools, use a *Catch Webhook* trigger on its `/sync` URL with *Return Response*.

## Safety

- Use only voices you own or have permission to use. Don't clone a real person's voice without written consent.
- Tell callers they are talking to an AI agent and that calls may be recorded, if that applies where you operate.
- Keep the shared secret and webhook secret in n8n, not in the agent prompt.
