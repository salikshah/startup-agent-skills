# Hacker News 'Who is hiring?' scraper and parser

**Platform:** n8n  |  **Category:** ops  |  **Maps to skill:** traction-channel-prioritization

Finds the latest 'Ask HN: Who is hiring?' threads via Algolia, pulls every top-level comment from the HN API, GPT-4o-mini turns each into structured fields (company, title, location, type, salary, apply link), saves to Airtable.

## Source and license

- Original author: Julian Kaiser (jksr)
- Original source: https://n8n.io/workflows/2924
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `Hacker News Job Listing Scraper and Parser.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Manual, Split Out, OpenAI Chat Model, Structured Output Parser, HTTP Request, Edit Fields, Filter, Basic LLM Chain, Code, Limit, Airtable

## Credentials

- Header Auth for the Algolia search call (see sticky note), or switch the node to the public `https://hn.algolia.com/api/v1/search_by_date` endpoint which needs no key
- OpenAI API
- Airtable

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Follow the sticky notes to set up the Algolia call.
2. Create the Airtable table with the fields listed in the *Data Structure* note, or replace Airtable with Google Sheets.

## How to test

Click *Test workflow* with the Limit node set to 5 comments first.
