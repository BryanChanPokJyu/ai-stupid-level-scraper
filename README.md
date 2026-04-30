# AI Stupid Level Tracker

> Auto-updated: 2026-04-30 17:52:20 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-opus-4-5-20251101 | 63 | ➡️ | anthropic |
| 2 | deepseek-chat | 62 | ➡️ | deepseek |
| 3 | gpt-5.2 | 62 | ➡️ | openai |
| 4 | claude-sonnet-4-6 | 62 | 📈 | anthropic |
| 5 | claude-sonnet-4-5-20250929 | 61 | 📈 | anthropic |
| 6 | kimi-k2-turbo-preview | 61 | ➡️ | kimi |
| 7 | gpt-5.5 | 61 | ➡️ | openai |
| 8 | claude-opus-4-1-20250805 | 60 | ➡️ | anthropic |
| 9 | claude-opus-4-6 | 60 | ➡️ | anthropic |
| 10 | claude-opus-4-7 | 60 | ➡️ | anthropic |
| 11 | kimi-latest | 59 | ➡️ | kimi |
| 12 | kimi-k2-0905-preview | 58 | ➡️ | kimi |
| 13 | gpt-5.3-codex | 58 | ➡️ | openai |
| 14 | grok-code-fast-1 | 50 | 📈 | xai |
| 15 | gemini-3-pro-preview | 50 | 📉 | google |
| 16 | claude-sonnet-4-20250514 | 46 | 📉 | anthropic |
| 17 | grok-4-0709 | 43 | ➡️ | xai |
| 18 | gemini-2.5-flash | 40 | ➡️ | google |
| 19 | deepseek-reasoner | 38 | 📉 | deepseek |
| 20 | gpt-5.4 | 38 | 📉 | openai |
| 21 | kimi-thinking-preview | 37 | ➡️ | kimi |
| 22 | glm-4.6 | 36 | ➡️ | glm |
| 23 | glm-4.7 | 36 | ➡️ | glm |
| 24 | grok-4-latest | 33 | 📉 | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
