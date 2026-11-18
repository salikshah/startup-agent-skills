# Job and opportunity alerts from ATS boards (Activepieces)

**Platform:** Activepieces  |  **Category:** ops  |  **Maps to skill:** traction-channel-prioritization, deep-work-protocol  |  **n8n equivalent:** `n8n/ops/job-opportunity-alerts.json`

Daily digest of new matching roles from Greenhouse, Lever and Ashby public boards, visa-sponsorship mentions flagged.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Schedule (*Every Day*)
- Loop on Items
- HTTP
- Code
- Storage (*Get*/*Put*) for seen URLs
- Telegram Bot or Gmail

## Steps

1. *Schedule > Every Day* 07:00.
2. *Code*: build the list of board URLs (`https://boards-api.greenhouse.io/v1/boards/<id>/jobs?content=true`, `https://api.lever.co/v0/postings/<id>?mode=json`, `https://api.ashbyhq.com/posting-api/job-board/<id>`).
3. *Loop on Items* -> *HTTP* GET each (continue on failure).
4. *Code*: normalise the three formats, filter by title keywords, locations and age, flag `sponsorship_mentioned` when the description contains your visa terms.
5. *Storage > Get* seen URLs, drop them, *Storage > Put* the new list.
6. *Telegram Bot > Send Text Message* (or *Gmail > Send Email* to yourself) with the digest.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Headhunter (recruiting-side reference)](https://cloud.activepieces.com/templates/kgSgS8CsiQNWo3MUxZjP0) (`kgSgS8CsiQNWo3MUxZjP0`)

## Notes

No API keys needed for these public board APIs. The flow never applies on your behalf.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
