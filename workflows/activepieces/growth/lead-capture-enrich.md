# Lead capture, enrichment and ICP scoring (Activepieces)

**Platform:** Activepieces  |  **Category:** growth  |  **Maps to skill:** traction-channel-prioritization, category-positioning-sop  |  **n8n equivalent:** `n8n/growth/lead-capture-enrich-crm.json`

Inbound form lead -> homepage research -> ICP score -> sheet/CRM upsert -> Slack alert.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Webhook
- Code
- HTTP
- AI (*Extract Structured Data*)
- Google Sheets (*Find or Create Row* / *Update Row*) or HubSpot (*Create or Update Contact*)
- Slack (*Send Message To A Channel*)

## Steps

1. *Webhook > Catch Webhook* from your site form.
2. *Code*: lowercase and validate email, drop honeypot submissions, derive the website from the email domain unless it is a free-mail domain.
3. *HTTP* GET the homepage (enable *continue on failure*), *Code* to strip HTML to ~6,000 chars.
4. *AI > Extract Structured Data*: `company_summary`, `industry`, `company_size_guess`, `icp_fit` (0-100), `fit_reason`, `next_step`. Put your ICP in the prompt and forbid guessing numbers.
5. *Google Sheets > Find or Create Row* on email, then *Update Row*; or *HubSpot > Create or Update Contact*.
6. *Router*: `icp_fit >= 70` -> *Slack > Send Message To A Channel*.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Score and Qualify Inbound Leads](https://cloud.activepieces.com/templates/8hyXTVZhdcFrK3hYlA6sM) (`8hyXTVZhdcFrK3hYlA6sM`)
- [Enrich Company Data for Leads](https://cloud.activepieces.com/templates/4UWOfYZWzp1xUGM0uWO5O) (`4UWOfYZWzp1xUGM0uWO5O`)
- [Auto-Qualify & Enrich Leads into HubSpot](https://cloud.activepieces.com/templates/aTsXyjLnFUaNhK2YP2qfm) (`aTsXyjLnFUaNhK2YP2qfm`)

## Notes

Perplexity-based gallery templates add web research; keep a cost cap if you use them on every form fill.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
