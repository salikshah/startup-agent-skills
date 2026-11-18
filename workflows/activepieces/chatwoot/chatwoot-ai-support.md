# Chatwoot AI support agent with human handoff (Activepieces)

**Platform:** Activepieces  |  **Category:** chatwoot  |  **Maps to skill:** aeo-geo-playbook, scaling-up-framework  |  **n8n equivalent:** `n8n/chatwoot/chatwoot-ai-support-agent.json`

Answer incoming Chatwoot messages from a knowledge base; hand off to a human when confidence is low.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Chatwoot (trigger *New Incoming Message*, action *Send Message*)
- HTTP (*Send HTTP Request*)
- AI (*Extract Structured Data*)
- Router
- Code

## Steps

1. **Trigger: Chatwoot > New Incoming Message.** Connect with your Chatwoot URL and an agent-bot or user access token. If your Activepieces version lacks the trigger, use *Webhook > Catch Webhook* and register that URL as an Agent Bot webhook in Chatwoot.
2. **Code: should the bot answer?** Return `{ skip: true }` when `message_type` is not `incoming`, the message is private, the conversation already has the `ai-handoff` label, or status is not `pending`. Follow with a *Router* branch that stops on `skip`.
3. **HTTP: GET** `{chatwoot}/api/v1/accounts/{account}/conversations/{id}/messages` with header `api_access_token`. Keep the last 12 messages.
4. **HTTP: GET** your FAQ file (raw markdown URL) as text.
5. **AI > Extract Structured Data** with fields `answer` (text), `confidence` (number 0-1), `needs_human` (boolean), `reason` (text). Prompt: answer only from the FAQ, set `needs_human` for refunds, billing, legal, account access or an upset customer.
6. **Router:** branch A when `confidence >= 0.75` and `needs_human` is false; branch B otherwise.
7. **Branch A: Chatwoot > Send Message** with the answer.
8. **Branch B:** *Chatwoot > Send Message* (holding reply) then three *HTTP* calls: POST `.../messages` with `private: true` (note with reason and draft), POST `.../labels` with `{"labels":["ai-handoff"]}`, POST `.../toggle_status` with `{"status":"open"}`.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Run Support Tickets From Slack (AI + Linear triage pattern)](https://cloud.activepieces.com/templates/XP05ahjcJygHimAunSObk) (`XP05ahjcJygHimAunSObk`)
- [Linear Support Agent](https://cloud.activepieces.com/templates/fdW2nXGk6VzcH5AezjxaG) (`fdW2nXGk6VzcH5AezjxaG`)

## Notes

Chatwoot's own *Captain* AI and Activepieces' Chatwoot piece cover the reply step; the handoff calls use the plain Chatwoot REST API so they work on any self-hosted version.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
