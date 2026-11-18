# Weekly metrics digest to Slack

**Platform:** n8n  |  **Category:** ops  |  **Maps to skill:** scaling-up-framework (weekly metrics rhythm), lean-startup-method (innovation accounting)

Weekly: reads a metrics sheet, computes week-over-week deltas in code, LLM writes headline/wins/concerns/focus, posts to Slack.

## Source and license

Original work for this repository (Salik Shah), MIT, same license as the repo.
Written for n8n 1.x (tested shape: n8n export format, `executionOrder: v1`).

## Nodes

Schedule, Edit Fields, Google Sheets, Code, Basic LLM Chain, OpenAI Chat Model, Structured Output Parser, Slack

## Credentials

- Google Sheets OAuth2
- OpenAI API
- Slack API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Tab `metrics`: column `week` (e.g. 2026-W47) + numeric columns + optional `notes`. Fill it by hand or from Stripe/PostHog workflows.
2. Set `north_star` and the Slack channel.
3. Activate.

## How to test

Add two weekly rows and click *Test workflow*; check the Slack message.

## Safety

Read-only on the sheet.
