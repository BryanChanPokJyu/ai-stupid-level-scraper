# AI Stupid Level Tracker

> Auto-updated: 2026-05-02 10:11:49 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-sonnet-4-5-20250929 | 64 | ➡️ | anthropic |
| 2 | deepseek-chat | 63 | 📈 | deepseek |
| 3 | claude-opus-4-5-20251101 | 63 | ➡️ | anthropic |
| 4 | claude-opus-4-7 | 63 | ➡️ | anthropic |
| 5 | gpt-5.2 | 62 | ➡️ | openai |
| 6 | claude-opus-4-6 | 62 | 📈 | anthropic |
| 7 | gpt-5.4 | 61 | ➡️ | openai |
| 8 | gpt-5.5 | 61 | ➡️ | openai |
| 9 | kimi-latest | 59 | ➡️ | kimi |
| 10 | claude-opus-4-1-20250805 | 57 | ➡️ | anthropic |
| 11 | gemini-3-pro-preview | 57 | 📉 | google |
| 12 | gpt-5.3-codex | 57 | ➡️ | openai |
| 13 | grok-4-latest | 47 | ➡️ | xai |
| 14 | claude-sonnet-4-20250514 | 46 | 📉 | anthropic |
| 15 | gemini-2.5-flash | 46 | ➡️ | google |
| 16 | claude-sonnet-4-6 | 46 | 📉 | anthropic |
| 17 | grok-4-0709 | 45 | 📈 | xai |
| 18 | glm-4.6 | 39 | ➡️ | glm |
| 19 | kimi-thinking-preview | 39 | ➡️ | kimi |
| 20 | glm-4.7 | 39 | ➡️ | glm |
| 21 | deepseek-reasoner | 38 | 📉 | deepseek |
| 22 | kimi-k2-0905-preview | 37 | ➡️ | kimi |
| 23 | kimi-k2-turbo-preview | 37 | ➡️ | kimi |
| 24 | grok-code-fast-1 | 36 | 📉 | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
