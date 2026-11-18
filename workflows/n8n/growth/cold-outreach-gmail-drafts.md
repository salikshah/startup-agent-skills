# Cold outreach: research each lead and write Gmail drafts

**Platform:** n8n  |  **Category:** growth  |  **Maps to skill:** traction-channel-prioritization (outbound test), growth-hacking-loop

Sheet of leads -> website research -> personalised email with a quoted fact and confidence score -> Gmail draft (never sent) -> row marked drafted / needs_research.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Manual, Schedule, Edit Fields, Google Sheets, Code, HTTP Request, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, If, Gmail

## Credentials

- Google Sheets OAuth2
- OpenAI API
- Gmail OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Sheet tab `leads` headers: email, first_name, company, website, notes, status, do_not_contact, drafted_at, personalization.
2. Fill `offer`, `proof`, `sender_name`. Keep `max_per_run` small so you can review every draft.
3. Check the cold-email rules where your recipients are (e.g. UK PECR, EU GDPR, US CAN-SPAM) before sending anything.

## How to test

Add two rows (one with a real company website, one with no website) and click *Test workflow*. Expect one Gmail draft and one `needs_research` row.

## Safety

No send operation exists in this workflow. Rows marked `do_not_contact = yes` are skipped.
