# Personalized cold email writer grounded in the lead's website (form-based)

**Platform:** n8n  |  **Category:** growth  |  **Maps to skill:** traction-channel-prioritization, growth-hacking-loop

n8n Form: enter a lead and their website; the workflow fetches the site, strips HTML, and an AI Agent writes a cold email shown on the completion page. Nothing is sent.

## Source and license

- Original author: contributor not named (added to enescingoz/awesome-n8n-templates on 2026-07-15)
- Original source: https://github.com/enescingoz/awesome-n8n-templates
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `Website-Grounded Cold Email Writer.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Form Trigger, HTTP Request, HTML, AI Agent, OpenAI Chat Model, Form

## Credentials

- OpenAI API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Select your OpenAI credential.
2. Activate and open the form URL.

## How to test

Open the form URL, enter a real company website, submit, copy the draft.
