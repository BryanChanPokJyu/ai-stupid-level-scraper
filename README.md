# AI Stupid Level Tracker

> Auto-updated: 2026-05-03 07:30:05 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-opus-4-6 | 69 | 📈 | anthropic |
| 2 | claude-opus-4-5-20251101 | 68 | ➡️ | anthropic |
| 3 | claude-sonnet-4-5-20250929 | 64 | ➡️ | anthropic |
| 4 | claude-sonnet-4-6 | 62 | ➡️ | anthropic |
| 5 | claude-opus-4-7 | 62 | ➡️ | anthropic |
| 6 | claude-sonnet-4-20250514 | 61 | ➡️ | anthropic |
| 7 | deepseek-chat | 61 | ➡️ | deepseek |
| 8 | deepseek-reasoner | 60 | 📈 | deepseek |
| 9 | gpt-5.4 | 60 | ➡️ | openai |
| 10 | gpt-5.5 | 59 | ➡️ | openai |
| 11 | kimi-latest | 57 | ➡️ | kimi |
| 12 | gpt-5.3-codex | 56 | ➡️ | openai |
| 13 | claude-opus-4-1-20250805 | 54 | 📈 | anthropic |
| 14 | gemini-3-pro-preview | 53 | 📉 | google |
| 15 | grok-code-fast-1 | 49 | ➡️ | xai |
| 16 | grok-4-latest | 47 | 📉 | xai |
| 17 | grok-4-0709 | 46 | 📈 | xai |
| 18 | gemini-2.5-flash | 44 | 📉 | google |
| 19 | kimi-thinking-preview | 41 | ➡️ | kimi |
| 20 | glm-4.6 | 40 | ➡️ | glm |
| 21 | glm-4.7 | 40 | ➡️ | glm |
| 22 | kimi-k2-turbo-preview | 39 | ➡️ | kimi |
| 23 | kimi-k2-0905-preview | 37 | ➡️ | kimi |
| 24 | gpt-5.2 | 37 | 📉 | openai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
