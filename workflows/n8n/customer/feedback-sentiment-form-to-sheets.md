# AI customer feedback sentiment analysis (form to Sheets)

**Platform:** n8n  |  **Category:** customer  |  **Maps to skill:** lean-startup-method

n8n Form collects feedback, OpenAI classifies sentiment, the merged record is appended to Google Sheets.

## Source and license

- Original author: MilanWR (milanwr)
- Original source: https://n8n.io/workflows/1996
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `AI Customer feedback sentiment analysis.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Google Sheets, Merge, OpenAI, Form Trigger

## Credentials

- OpenAI API
- Google Sheets OAuth2

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Copy the example sheet linked in the sticky note, select it in the Sheets node.
2. Activate and share the form URL.

## How to test

Submit the form twice (one happy, one angry) and check the sentiment column.
