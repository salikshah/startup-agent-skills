# Market and competitor RSS monitor (Activepieces)

**Platform:** Activepieces  |  **Category:** ops  |  **Maps to skill:** unicorn-pattern-analysis, category-positioning-sop  |  **n8n equivalent:** `n8n/ops/market-rss-monitor.json`

Relevant news from your feeds, scored for your market, one digest.

## Source and license

Original build guide for this repository (Salik Shah), MIT. Piece and action names were checked against the `activepieces/activepieces` repository (MIT community edition) on 2026-11-18; menus can be renamed between versions.

## Pieces

- RSS Feed (*New Item* trigger or *Read Multiple Feeds*)
- Storage (*Get* / *Put*) for dedupe
- AI (*Extract Structured Data*)
- Telegram Bot or Slack

## Steps

1. Simple version: one flow per feed with *RSS Feed > New Item* (the trigger dedupes for you) -> *AI > Extract Structured Data* (`score` 0-10, `why`, `content_angle`) -> *Router* `score >= 7` -> *Telegram Bot > Send Text Message*.
2. Digest version: *Schedule > Every X Hours* -> *RSS Feed > Read Multiple Feeds* -> *Storage > Get* the list of seen links -> *Code* drop seen, keyword and age filter, keep 25 -> *Loop on Items* with the AI step -> *Code* build one message -> send -> *Storage > Put* the updated seen list.

## Starting points in the Activepieces template gallery

These official templates cover part of the flow. Open the link, click *Use template*, then change it to match the steps above. They are linked, not copied, because the gallery does not state a license for template content.

- [RSS Feed Reader (Daily Digest Creator)](https://cloud.activepieces.com/templates/zoSZlMcXmnQSmlC1OIjkL) (`zoSZlMcXmnQSmlC1OIjkL`)
- [Automated RSS Monitoring with Gemini AI Summaries to Google Sheets](https://cloud.activepieces.com/templates/CyLrLY0axR056XmyyCpcb) (`CyLrLY0axR056XmyyCpcb`)
- [Gather Latest Industry News](https://cloud.activepieces.com/templates/M7HSNDiMR4rUyAGcogtQr) (`M7HSNDiMR4rUyAGcogtQr`)

## Notes

Google News RSS (`https://news.google.com/rss/search?q=<query>`) turns any search into a feed.

## Safety

Keep drafts as drafts and keep a human approval step before anything irreversible (sending email, posting publicly, changing customer records).
