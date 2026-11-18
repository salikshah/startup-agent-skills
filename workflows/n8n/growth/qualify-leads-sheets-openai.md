# Qualify new leads in Google Sheets via OpenAI

**Platform:** n8n  |  **Category:** growth  |  **Maps to skill:** traction-channel-prioritization

Google Sheets trigger on new row (e.g. from Google Forms), OpenAI qualifies the lead against your instructions, result is written back to the row.

## Source and license

- Original author: Yulia (yulia)
- Original source: https://n8n.io/workflows/2163
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `Qualify new leads in Google Sheets via OpenAI_s GPT-4.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Merge, Google Sheets, Edit Fields, OpenAI, Google Sheets Trigger

## Credentials

- Google Sheets Trigger OAuth2 + Google Sheets OAuth2
- OpenAI API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Copy the sheet template linked in the sticky note or point the trigger at your own sheet.
2. Edit the system message with your qualification criteria and set the *Column to match on*.

## How to test

Add a row to the sheet; within a minute the qualification column fills in.
