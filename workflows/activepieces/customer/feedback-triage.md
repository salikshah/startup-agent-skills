# Customer feedback triage (Activepieces)

**Platform:** Activepieces  |  **Category:** customer  |  **Maps to skill:** lean-startup-method, growth-hacking-loop  |  **n8n equivalent:** `n8n/customer/customer-feedback-triage.json`

Classify feedback, log it, route bugs and churn risks, draft replies.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Webhook / Forms / Typeform
- AI (*Classify Text*, *Extract Structured Data*)
- Google Sheets
- Router
- Slack
- Gmail (*Create Draft*)

## Steps

1. Trigger on your source (*Webhook*, *Typeform > New Submission*, *Gmail > New Email* with a label).
2. *AI > Extract Structured Data*: `type` (bug, feature_request, churn_risk, question, praise, other), `severity` 1-5, `product_area`, `summary`, `customer_quote`, `suggested_reply`.
3. *Google Sheets > Insert Row* into `feedback`.
4. *Router*: bug -> *Slack* bugs channel; churn_risk -> *Slack* customer channel + *Gmail > Create Draft* to the customer with the suggested reply.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Create Linear Issues From Support Emails](https://cloud.activepieces.com/templates/rnuOkGmfZO2BHpAjsRMLk) (`rnuOkGmfZO2BHpAjsRMLk`)
- [Monitor Discord/Slack and Surface Issues](https://cloud.activepieces.com/templates/TbObAly8gAIP5O8dgvE7G) (`TbObAly8gAIP5O8dgvE7G`)
- [Turn Product Reviews Into Content Ideas](https://cloud.activepieces.com/templates/TNzlJSjn1QEz7xSnotxdp) (`TNzlJSjn1QEz7xSnotxdp`)

## Notes

Use *AI > Classify Text* when you only need the label; it is cheaper than structured extraction.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
