# AI Stupid Level Tracker

> Auto-updated: 2026-04-30 21:35:12 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | gemini-3-pro-preview | 64 | 📈 | google |
| 2 | claude-sonnet-4-20250514 | 62 | 📉 | anthropic |
| 3 | claude-sonnet-4-5-20250929 | 62 | ➡️ | anthropic |
| 4 | deepseek-chat | 62 | ➡️ | deepseek |
| 5 | kimi-k2-turbo-preview | 62 | 📈 | kimi |
| 6 | claude-opus-4-5-20251101 | 62 | ➡️ | anthropic |
| 7 | claude-sonnet-4-6 | 62 | 📉 | anthropic |
| 8 | gpt-5.2 | 61 | ➡️ | openai |
| 9 | gpt-5.4 | 61 | ➡️ | openai |
| 10 | claude-opus-4-7 | 61 | ➡️ | anthropic |
| 11 | gpt-5.5 | 61 | ➡️ | openai |
| 12 | claude-opus-4-1-20250805 | 60 | ➡️ | anthropic |
| 13 | claude-opus-4-6 | 60 | ➡️ | anthropic |
| 14 | kimi-k2-0905-preview | 59 | 📈 | kimi |
| 15 | kimi-latest | 59 | ➡️ | kimi |
| 16 | gpt-5.3-codex | 58 | ➡️ | openai |
| 17 | grok-4-latest | 46 | 📈 | xai |
| 18 | grok-4-0709 | 43 | ➡️ | xai |
| 19 | gemini-2.5-flash | 41 | ➡️ | google |
| 20 | deepseek-reasoner | 40 | ➡️ | deepseek |
| 21 | kimi-thinking-preview | 37 | ➡️ | kimi |
| 22 | glm-4.6 | 36 | ➡️ | glm |
| 23 | glm-4.7 | 36 | ➡️ | glm |
| 24 | grok-code-fast-1 | 32 | 📉 | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
