# Weekly metrics digest (Activepieces)

**Platform:** Activepieces  |  **Category:** ops  |  **Maps to skill:** scaling-up-framework, lean-startup-method  |  **n8n equivalent:** `n8n/ops/weekly-metrics-digest.json`

Monday note: week-over-week deltas computed in code, narrative by AI, posted to Slack.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Schedule (*Every Week*)
- Google Sheets (*Get Rows*)
- Code
- AI (*Ask AI*)
- Slack

## Steps

1. *Schedule > Every Week*, Monday 08:00.
2. *Google Sheets > Get Rows* from `metrics` (one row per week).
3. *Code*: take the last two rows, compute change per numeric column. Do the arithmetic here, not in the model.
4. *AI > Ask AI*: headline, wins, concerns, one focus, questions. Pass only the computed table.
5. *Slack > Send Message To A Channel*.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Produce Weekly Business Reports Automatically](https://cloud.activepieces.com/templates/UZOVDYrJoNbneQR9RhFsb) (`UZOVDYrJoNbneQR9RhFsb`)
- [Weekly Business Review](https://cloud.activepieces.com/templates/CAhsBJ0KMnD29caEa8eD6) (`CAhsBJ0KMnD29caEa8eD6`)
- [Daily KPI Trend Chart -> Slack](https://cloud.activepieces.com/templates/auR0JMrF3FcaqZjxTIc9x) (`auR0JMrF3FcaqZjxTIc9x`)

## Notes

Stripe and HubSpot pieces can fill the sheet automatically in a separate daily flow.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
