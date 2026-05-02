# AI Stupid Level Tracker

> Auto-updated: 2026-05-02 17:32:39 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-sonnet-4-5-20250929 | 64 | ➡️ | anthropic |
| 2 | claude-opus-4-5-20251101 | 63 | 📈 | anthropic |
| 3 | claude-opus-4-7 | 63 | 📈 | anthropic |
| 4 | deepseek-chat | 62 | ➡️ | deepseek |
| 5 | gpt-5.2 | 62 | ➡️ | openai |
| 6 | gpt-5.4 | 62 | 📈 | openai |
| 7 | gpt-5.5 | 61 | ➡️ | openai |
| 8 | deepseek-reasoner | 60 | 📈 | deepseek |
| 9 | claude-opus-4-6 | 60 | ➡️ | anthropic |
| 10 | kimi-latest | 59 | ➡️ | kimi |
| 11 | gpt-5.3-codex | 58 | ➡️ | openai |
| 12 | claude-sonnet-4-20250514 | 56 | ➡️ | anthropic |
| 13 | claude-sonnet-4-6 | 55 | ➡️ | anthropic |
| 14 | grok-4-latest | 49 | 📈 | xai |
| 15 | gemini-3-pro-preview | 46 | 📉 | google |
| 16 | claude-opus-4-1-20250805 | 45 | 📉 | anthropic |
| 17 | grok-4-0709 | 44 | ➡️ | xai |
| 18 | glm-4.6 | 39 | ➡️ | glm |
| 19 | kimi-thinking-preview | 39 | ➡️ | kimi |
| 20 | glm-4.7 | 39 | ➡️ | glm |
| 21 | kimi-k2-0905-preview | 37 | 📉 | kimi |
| 22 | kimi-k2-turbo-preview | 37 | 📉 | kimi |
| 23 | gemini-2.5-flash | 36 | ➡️ | google |
| 24 | grok-code-fast-1 | 34 | 📉 | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
