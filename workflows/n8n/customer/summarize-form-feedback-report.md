# Summarize Google Sheets form feedback via OpenAI into an emailed report

**Platform:** n8n  |  **Category:** customer  |  **Maps to skill:** lean-startup-method

Reads all form responses from a Google Sheet, aggregates answers per question, OpenAI writes a Markdown summary report, converted to HTML and emailed with Gmail.

## Source and license

- Original author: Yulia (yulia)
- Original source: https://n8n.io/workflows/2164
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `Summarize Google Sheets form feedback via OpenAI_s GPT-4.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Manual, Google Sheets, Aggregate, OpenAI, Markdown, Gmail

## Credentials

- Google Sheets OAuth2
- OpenAI API
- Gmail OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Copy the sheet template linked in the sticky note or point the Sheets node at your responses sheet.
2. Set the recipient in the Gmail node to your own address (it sends one internal report email to you; it is not customer-facing).

## How to test

Click *Test workflow*; check your inbox for the HTML report.
