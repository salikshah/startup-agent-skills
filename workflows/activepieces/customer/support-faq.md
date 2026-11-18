# Support FAQ answers (Activepieces)

**Platform:** Activepieces  |  **Category:** customer  |  **Maps to skill:** aeo-geo-playbook  |  **n8n equivalent:** `n8n/customer/support-faq-rag-chat.json`

Answer FAQ questions from your docs in chat, Slack or email.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Forms (*Chat Trigger*) or Slack (*New Mention*)
- AI (*Run Agent* or *Ask AI*)
- HTTP or Tables (knowledge source)
- Webhook / Forms *Return Response*

## Steps

1. *Forms > Chat Trigger* gives you a hosted chat page; or trigger on a Slack mention.
2. Load knowledge: *HTTP* GET a markdown FAQ, or *Tables > Find Records* from a table of Q&A pairs.
3. *AI > Ask AI* with the FAQ in the prompt and the rule "answer only from this; otherwise say you are not sure and give the support email". For larger docs use *AI > Run Agent* with an HTTP tool that searches your Qdrant collection (`POST /collections/support_kb/points/search`).
4. *Forms > Return Response* (chat) or *Slack > Send Message* in thread.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Answer Employee Policy Questions Instantly](https://cloud.activepieces.com/templates/9CssQ40xsg1WT0cR6mzYU) (`9CssQ40xsg1WT0cR6mzYU`)

## Notes

Activepieces has no built-in vector-store piece in the community edition list we checked; the HTTP call to Qdrant's search API fills that gap.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
