# Post-eval gate with human approval (Activepieces)

**Platform:** Activepieces  |  **Category:** content  |  **Maps to skill:** post-eval  |  **n8n equivalent:** `n8n/content/post-eval-gate.json`

Score a draft with the post-eval rubric and queue it only after a human approves.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- Webhook
- AI (*Extract Structured Data*)
- Code
- Router
- Gmail (*Request Approval in Email*) or Approval (*Create Approval Links* + *Wait for Approval*)
- Google Sheets
- X / LinkedIn (optional)

## Steps

1. *Webhook > Catch Webhook* with `draft`, `platform`, optional `proof_url`.
2. *AI > Extract Structured Data*: integer fields `strategic_alignment` (0-20), `proof_of_work` (0-25), `content_quality` (0-20), `timing` (0-15), `risk` (0-20) plus `pros`, `cons`, `recommendation`, `rewrite`. Paste the rubric from `skills/00-post-eval/post-eval/SKILL.md` into the prompt.
3. *Code*: clamp scores, cap proof of work at 10 when there is no link, fail X drafts over 280 chars and LinkedIn over 1,500, total the score, verdict = POST when total >= 70.
4. *Webhook > Return Response* with the verdict JSON (use the `/sync` webhook URL).
5. *Router*: only POST verdicts continue -> *Gmail > Request Approval in Email* to yourself (or *Approval > Create Approval Links* + *Wait for Approval*).
6. Approved -> *Google Sheets > Insert Row* in `publish_queue`. Add *X > Create Tweet* only if you want approved posts to go out automatically.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [Block Risky Content Before It Goes Live](https://cloud.activepieces.com/templates/VWsl3kKOYNjB8YLE9lcPg) (`VWsl3kKOYNjB8YLE9lcPg`)
- [Newsletter Approval Workflow](https://cloud.activepieces.com/templates/7Js4K8WufOaSSSd2uPpdg) (`7Js4K8WufOaSSSd2uPpdg`)
- [Content Quality Gate for SEO Agencies](https://cloud.activepieces.com/templates/DgxaE49fb4QRQwsnroWkE) (`DgxaE49fb4QRQwsnroWkE`)

## Notes

Keep the approval step even when the score passes; the rubric is a filter, not a publisher.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
