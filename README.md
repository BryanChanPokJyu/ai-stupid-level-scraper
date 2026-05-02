# AI Stupid Level Tracker

> Auto-updated: 2026-05-02 14:15:51 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-sonnet-4-5-20250929 | 63 | 📈 | anthropic |
| 2 | claude-opus-4-5-20251101 | 63 | ➡️ | anthropic |
| 3 | claude-opus-4-6 | 63 | 📈 | anthropic |
| 4 | claude-opus-4-7 | 63 | ➡️ | anthropic |
| 5 | deepseek-chat | 62 | ➡️ | deepseek |
| 6 | gpt-5.2 | 62 | ➡️ | openai |
| 7 | gpt-5.4 | 62 | 📈 | openai |
| 8 | gpt-5.5 | 61 | ➡️ | openai |
| 9 | deepseek-reasoner | 60 | 📈 | deepseek |
| 10 | kimi-latest | 59 | ➡️ | kimi |
| 11 | gpt-5.3-codex | 58 | ➡️ | openai |
| 12 | claude-sonnet-4-20250514 | 57 | ➡️ | anthropic |
| 13 | gemini-3-pro-preview | 57 | 📈 | google |
| 14 | claude-opus-4-1-20250805 | 56 | 📈 | anthropic |
| 15 | grok-4-latest | 49 | 📈 | xai |
| 16 | claude-sonnet-4-6 | 47 | 📉 | anthropic |
| 17 | gemini-2.5-flash | 45 | ➡️ | google |
| 18 | grok-4-0709 | 44 | ➡️ | xai |
| 19 | glm-4.6 | 39 | ➡️ | glm |
| 20 | kimi-thinking-preview | 39 | ➡️ | kimi |
| 21 | glm-4.7 | 39 | ➡️ | glm |
| 22 | kimi-k2-0905-preview | 37 | 📉 | kimi |
| 23 | kimi-k2-turbo-preview | 37 | 📉 | kimi |
| 24 | grok-code-fast-1 | 34 | 📉 | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
