# Repurpose one post into an X thread + LinkedIn post (Activepieces)

**Platform:** Activepieces  |  **Category:** content  |  **Maps to skill:** content-strategy-framework, doing-content-right-sop  |  **n8n equivalent:** `n8n/content/content-repurpose-post-to-threads.json`

Turn one source (text or URL) into platform drafts stored for review.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Webhook or Forms
- HTTP
- AI (*Extract Structured Data*)
- Google Sheets or Tables

## Steps

1. *Forms > Form Trigger* (fields: text, url, angle) or *Webhook*.
2. *Router*: if `url` is set, *HTTP > Send HTTP Request* GET it, then *Code* to strip HTML.
3. *AI > Extract Structured Data*: `x_thread` (list of strings, each under 270 chars), `linkedin_post`, `hooks` (3). Tell the model to keep every claim traceable to the source.
4. *Code*: flag tweets over 280 chars.
5. *Google Sheets > Insert Row* (or *Tables > Create Records*) with status `draft`. Send each draft to the post-eval gate before publishing.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Repurpose RSS Feeds Into Social Posts](https://cloud.activepieces.com/templates/KGznJmYSoZtlUkHgAy44Y) (`KGznJmYSoZtlUkHgAy44Y`)
- [Discover and Repurpose LinkedIn Content Automatically](https://cloud.activepieces.com/templates/6IQyRhIKzabmIA3OIeBsX) (`6IQyRhIKzabmIA3OIeBsX`)
- [Tweet new WordPress posts with ChatGPT](https://cloud.activepieces.com/templates/zebhxZfmykfYRLilbQnWF) (`zebhxZfmykfYRLilbQnWF`)

## Notes

Several gallery templates post directly to LinkedIn/X. Replace the publish step with a sheet row or an approval step.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
