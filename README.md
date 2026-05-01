# AI Stupid Level Tracker

> Auto-updated: 2026-05-01 22:36:28 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | gemini-3-pro-preview | 72 | 📈 | google |
| 2 | claude-sonnet-4-20250514 | 65 | 📈 | anthropic |
| 3 | claude-opus-4-5-20251101 | 65 | ➡️ | anthropic |
| 4 | claude-sonnet-4-5-20250929 | 64 | ➡️ | anthropic |
| 5 | deepseek-chat | 64 | ➡️ | deepseek |
| 6 | claude-sonnet-4-6 | 64 | 📈 | anthropic |
| 7 | gpt-5.2 | 63 | ➡️ | openai |
| 8 | gpt-5.4 | 63 | 📈 | openai |
| 9 | claude-opus-4-7 | 63 | 📈 | anthropic |
| 10 | claude-opus-4-1-20250805 | 62 | ➡️ | anthropic |
| 11 | gpt-5.5 | 62 | ➡️ | openai |
| 12 | kimi-latest | 61 | ➡️ | kimi |
| 13 | claude-opus-4-6 | 61 | 📉 | anthropic |
| 14 | gpt-5.3-codex | 59 | ➡️ | openai |
| 15 | grok-code-fast-1 | 54 | 📈 | xai |
| 16 | grok-4-latest | 49 | 📈 | xai |
| 17 | gemini-2.5-flash | 48 | 📉 | google |
| 18 | grok-4-0709 | 41 | 📉 | xai |
| 19 | glm-4.6 | 40 | ➡️ | glm |
| 20 | deepseek-reasoner | 40 | 📈 | deepseek |
| 21 | kimi-thinking-preview | 40 | ➡️ | kimi |
| 22 | glm-4.7 | 40 | ➡️ | glm |
| 23 | kimi-k2-turbo-preview | 38 | ➡️ | kimi |
| 24 | kimi-k2-0905-preview | 35 | 📉 | kimi |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
