# Customer support channel and ticketing with Slack and Linear

**Platform:** n8n  |  **Category:** customer  |  **Maps to skill:** scaling-up-framework

Polls a Slack support channel for messages tagged with the ticket emoji, skips ones already ticketed, LLM writes title/summary/priority, creates a Linear issue.

## Source and license

- Original author: Jimleuk (jimleuk)
- Original source: https://n8n.io/workflows/2323
- Copied from: https://github.com/enescingoz/awesome-n8n-templates (file `Customer Support Channel and Ticketing System with Slack and Linear.json`), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
- Status: **adapted**. Changes: credential IDs replaced with placeholders, pinned data and instance metadata removed, hardcoded recipient email addresses replaced with `you@example.com`, a *Source and license* sticky note added. Workflow logic is unchanged.
- Note: the n8n.io template library does not attach a license to individual templates; the CC BY 4.0 grant comes from the collection maintainer. Keep the attribution if you redistribute.

## Nodes

Slack, OpenAI Chat Model, Structured Output Parser, Schedule, Edit Fields, If, Linear, Basic LLM Chain, Merge, Aggregate

## Credentials

- Slack API
- Linear API
- OpenAI API

All credential IDs in the JSON are the placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID`. After import, open each node with a warning and pick your own credential.

## Setup

1. Set the Slack channel and the Linear team (both marked Required in sticky notes).
2. Activate; react with the ticket emoji on a message to create an issue.

## How to test

Post a test message in the channel, add the ticket emoji, run the workflow.
