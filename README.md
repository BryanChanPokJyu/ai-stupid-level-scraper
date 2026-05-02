# AI Stupid Level Tracker

> Auto-updated: 2026-05-02 23:27:16 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-opus-4-5-20251101 | 66 | 📈 | anthropic |
| 2 | claude-opus-4-7 | 65 | ➡️ | anthropic |
| 3 | claude-sonnet-4-5-20250929 | 64 | ➡️ | anthropic |
| 4 | deepseek-chat | 61 | ➡️ | deepseek |
| 5 | gpt-5.4 | 61 | ➡️ | openai |
| 6 | gpt-5.5 | 61 | ➡️ | openai |
| 7 | gpt-5.2 | 60 | ➡️ | openai |
| 8 | gemini-3-pro-preview | 59 | 📉 | google |
| 9 | kimi-latest | 58 | ➡️ | kimi |
| 10 | claude-opus-4-6 | 58 | ➡️ | anthropic |
| 11 | gpt-5.3-codex | 57 | ➡️ | openai |
| 12 | claude-sonnet-4-20250514 | 55 | ➡️ | anthropic |
| 13 | claude-sonnet-4-6 | 53 | 📉 | anthropic |
| 14 | grok-4-0709 | 52 | 📈 | xai |
| 15 | claude-opus-4-1-20250805 | 47 | 📉 | anthropic |
| 16 | grok-code-fast-1 | 47 | 📈 | xai |
| 17 | gemini-2.5-flash | 46 | 📉 | google |
| 18 | grok-4-latest | 42 | ➡️ | xai |
| 19 | glm-4.6 | 39 | ➡️ | glm |
| 20 | kimi-thinking-preview | 39 | ➡️ | kimi |
| 21 | glm-4.7 | 39 | ➡️ | glm |
| 22 | kimi-k2-0905-preview | 37 | ➡️ | kimi |
| 23 | kimi-k2-turbo-preview | 37 | ➡️ | kimi |
| 24 | deepseek-reasoner | 36 | 📉 | deepseek |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
