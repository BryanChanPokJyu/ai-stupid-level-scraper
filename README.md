# AI Stupid Level Tracker

> Auto-updated: 2026-04-30 11:45:33 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-sonnet-4-20250514 | 62 | ➡️ | anthropic |
| 2 | claude-sonnet-4-5-20250929 | 62 | ➡️ | anthropic |
| 3 | deepseek-reasoner | 62 | ➡️ | deepseek |
| 4 | claude-opus-4-5-20251101 | 62 | 📈 | anthropic |
| 5 | claude-sonnet-4-6 | 62 | ➡️ | anthropic |
| 6 | deepseek-chat | 61 | ➡️ | deepseek |
| 7 | gpt-5.2 | 61 | ➡️ | openai |
| 8 | gpt-5.4 | 61 | ➡️ | openai |
| 9 | gpt-5.5 | 61 | ➡️ | openai |
| 10 | claude-opus-4-6 | 60 | ➡️ | anthropic |
| 11 | claude-opus-4-7 | 60 | ➡️ | anthropic |
| 12 | kimi-latest | 58 | ➡️ | kimi |
| 13 | gpt-5.3-codex | 58 | ➡️ | openai |
| 14 | gemini-3-pro-preview | 56 | ➡️ | google |
| 15 | grok-4-latest | 44 | 📉 | xai |
| 16 | grok-code-fast-1 | 43 | 📉 | xai |
| 17 | kimi-k2-turbo-preview | 39 | ➡️ | kimi |
| 18 | claude-opus-4-1-20250805 | 38 | 📉 | anthropic |
| 19 | gemini-2.5-flash | 38 | 📈 | google |
| 20 | kimi-k2-0905-preview | 37 | ➡️ | kimi |
| 21 | kimi-thinking-preview | 37 | ➡️ | kimi |
| 22 | glm-4.6 | 36 | ➡️ | glm |
| 23 | glm-4.7 | 36 | ➡️ | glm |
| 24 | grok-4-0709 | 30 | 📉 | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
