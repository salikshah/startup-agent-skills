# Article to X thread + LinkedIn post (grounded, form-based)

**Platform:** n8n  |  **Category:** content  |  **Maps to skill:** content-strategy-framework, doing-content-right-sop, post-eval

n8n Form: paste an article or transcript, an AI Agent writes an X thread and a LinkedIn post grounded only in the source, shown on the completion page.

## Source and license

- Original author: contributor not named (added to enescingoz/awesome-n8n-templates on 2026-07-15)
- Original source: https://github.com/enescingoz/awesome-n8n-templates
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `Grounded Article to Thread and LinkedIn Post.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Form Trigger, AI Agent, OpenAI Chat Model, Form

## Credentials

- OpenAI API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Select your OpenAI credential on the chat model node.
2. Activate and open the form URL.

## How to test

Open the form URL from the Form Trigger node, paste 500+ words, submit.
