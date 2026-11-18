# Voice RAG chatbot with ElevenLabs and OpenAI (Qdrant)

**Platform:** n8n  |  **Category:** voice  |  **Maps to skill:** aeo-geo-playbook, scaling-up-framework

ElevenLabs Conversational AI agent calls an n8n webhook tool; an n8n AI Agent answers from a Qdrant collection built from Google Drive documents. Includes the collection setup and the website widget snippet.

## Source and license

- Original author: Davide Boizza (n3witalia)
- Original source: https://n8n.io/workflows/2846
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `AI Voice Chatbot with ElevenLabs & OpenAI for Customer Service and Restaurants.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

AI Agent, Vector Store Tool, Qdrant, OpenAI Embeddings, Manual, HTTP Request, Google Drive, Document Loader, Token Splitter, Respond to Webhook, OpenAI Chat Model, Webhook, Window Memory

## Credentials

- OpenAI API
- Qdrant API + Header Auth for Qdrant REST calls
- Google Drive OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Replace QDRANTURL and COLLECTION in the HTTP and Qdrant nodes (starter kit: `http://qdrant:6333`).
2. Follow the sticky notes STEP 1-5: create the ElevenLabs agent and its webhook tool pointing at `/webhook/test_voice_message_elevenlabs`.

## How to test

Click *Test workflow*, then *Test AI agent* in ElevenLabs and ask a question covered by your documents.
