# Cold outreach as Gmail drafts, never auto-sent (Activepieces)

**Platform:** Activepieces  |  **Category:** growth  |  **Maps to skill:** traction-channel-prioritization, growth-hacking-loop  |  **n8n equivalent:** `n8n/growth/cold-outreach-gmail-drafts.json`

Research each lead and save a personalised email as a Gmail draft for human review.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Schedule (*Every Day*) or Manual Trigger
- Google Sheets (*Find Rows*, *Update Row*)
- Loop on Items
- HTTP
- AI (*Extract Structured Data*)
- Gmail (*Create Draft*)

## Steps

1. *Schedule > Every Day* (weekdays) or *Manual Trigger*.
2. *Google Sheets > Find Rows* where `status` is empty; *Code* to skip `do_not_contact = yes` and keep the first 10.
3. *Loop on Items*: *HTTP* GET the website (continue on failure) -> *Code* strip HTML -> *AI > Extract Structured Data* (`subject`, `body` under 110 words, `personalization_fact`, `confidence`).
4. *Router*: `confidence >= 0.6` -> *Gmail > Create Draft*; otherwise mark the row `needs_research`.
5. *Google Sheets > Update Row* with `status = drafted`.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Email Outreach Drafter Based on HubSpot Data](https://cloud.activepieces.com/templates/zRtLPeUmfX6z7P0um6I68) (`zRtLPeUmfX6z7P0um6I68`)
- [Human-Approved AI Outreach](https://cloud.activepieces.com/templates/YrkgoBPdfsUEL8atuyqb0) (`YrkgoBPdfsUEL8atuyqb0`)
- [Draft Personalized Email Replies](https://cloud.activepieces.com/templates/fS3eRz6t4vrI73UcWEUyu) (`fS3eRz6t4vrI73UcWEUyu`)

## Notes

Do not use *Gmail > Send Email* here. Check the cold-email rules that apply to your recipients before sending drafts.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
