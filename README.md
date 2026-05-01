# AI Stupid Level Tracker

> Auto-updated: 2026-05-01 15:34:51 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | gemini-3-pro-preview | 64 | ➡️ | google |
| 2 | claude-opus-4-5-20251101 | 64 | ➡️ | anthropic |
| 3 | claude-sonnet-4-20250514 | 63 | 📈 | anthropic |
| 4 | claude-sonnet-4-5-20250929 | 63 | ➡️ | anthropic |
| 5 | deepseek-chat | 63 | ➡️ | deepseek |
| 6 | claude-sonnet-4-6 | 63 | ➡️ | anthropic |
| 7 | gpt-5.4 | 63 | ➡️ | openai |
| 8 | claude-opus-4-1-20250805 | 62 | ➡️ | anthropic |
| 9 | gpt-5.2 | 62 | ➡️ | openai |
| 10 | claude-opus-4-7 | 62 | ➡️ | anthropic |
| 11 | gpt-5.5 | 62 | ➡️ | openai |
| 12 | claude-opus-4-6 | 61 | ➡️ | anthropic |
| 13 | kimi-latest | 60 | ➡️ | kimi |
| 14 | gpt-5.3-codex | 58 | ➡️ | openai |
| 15 | grok-4-latest | 52 | ➡️ | xai |
| 16 | gemini-2.5-flash | 52 | 📈 | google |
| 17 | grok-code-fast-1 | 47 | ➡️ | xai |
| 18 | glm-4.6 | 40 | ➡️ | glm |
| 19 | kimi-thinking-preview | 40 | ➡️ | kimi |
| 20 | glm-4.7 | 40 | ➡️ | glm |
| 21 | deepseek-reasoner | 39 | ➡️ | deepseek |
| 22 | kimi-k2-turbo-preview | 37 | 📉 | kimi |
| 23 | kimi-k2-0905-preview | 36 | 📉 | kimi |
| 24 | grok-4-0709 | 35 | ➡️ | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
