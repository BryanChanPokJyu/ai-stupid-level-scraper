# AI Stupid Level Tracker

> Auto-updated: 2026-05-02 20:03:03 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-opus-4-5-20251101 | 66 | 📈 | anthropic |
| 2 | claude-opus-4-6 | 64 | ➡️ | anthropic |
| 3 | gpt-5.2 | 63 | ➡️ | openai |
| 4 | claude-opus-4-7 | 63 | ➡️ | anthropic |
| 5 | deepseek-chat | 62 | ➡️ | deepseek |
| 6 | gemini-3-pro-preview | 62 | 📈 | google |
| 7 | gpt-5.4 | 62 | ➡️ | openai |
| 8 | gpt-5.5 | 61 | ➡️ | openai |
| 9 | deepseek-reasoner | 60 | 📈 | deepseek |
| 10 | kimi-latest | 60 | ➡️ | kimi |
| 11 | claude-sonnet-4-20250514 | 58 | ➡️ | anthropic |
| 12 | gpt-5.3-codex | 58 | ➡️ | openai |
| 13 | claude-opus-4-1-20250805 | 57 | ➡️ | anthropic |
| 14 | claude-sonnet-4-6 | 57 | ➡️ | anthropic |
| 15 | grok-4-0709 | 51 | 📈 | xai |
| 16 | claude-sonnet-4-5-20250929 | 51 | 📉 | anthropic |
| 17 | grok-code-fast-1 | 49 | 📈 | xai |
| 18 | grok-4-latest | 47 | ➡️ | xai |
| 19 | gemini-2.5-flash | 44 | ➡️ | google |
| 20 | glm-4.6 | 39 | ➡️ | glm |
| 21 | kimi-thinking-preview | 39 | ➡️ | kimi |
| 22 | glm-4.7 | 39 | ➡️ | glm |
| 23 | kimi-k2-turbo-preview | 38 | 📉 | kimi |
| 24 | kimi-k2-0905-preview | 37 | 📉 | kimi |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
