# Changelog

## Unreleased: workflows collection

- Added `workflows/`: 27 n8n workflow exports (17 original, 10 adapted from CC BY 4.0 sources with attribution) and 11 Activepieces build guides across six categories: chatwoot, voice, content, growth, customer, ops.
- Added recipes: `workflows/recipes/chatwoot-n8n-ai-support.md` (Docker Compose for Chatwoot + n8n + Postgres + Redis, Agent Bot wiring, handoff rule, curl test script, WhatsApp and Activepieces variants) and `workflows/recipes/elevenlabs-voice.md` (dictation to tasks, post to voiceover, voice agent calling n8n tools, post-call webhook).
- Added `workflows/CREDITS.md` with author, URL, license and adaptation status for every source.
- Added `workflows/tools/validate_workflows.py`, a zero-dependency validator (JSON shape, node types, connections, node references in expressions, placeholder credentials, secret scan, companion docs). It runs in CI.
- README: new *Workflows* section.

## 1.0.0

- Initial release of the startup agent skills.
