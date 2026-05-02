# AI Stupid Level Tracker

> Auto-updated: 2026-05-02 06:23:10 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-opus-4-1-20250805 | 65 | 📈 | anthropic |
| 2 | claude-sonnet-4-5-20250929 | 64 | ➡️ | anthropic |
| 3 | deepseek-chat | 61 | ➡️ | deepseek |
| 4 | gpt-5.2 | 61 | ➡️ | openai |
| 5 | gpt-5.5 | 61 | ➡️ | openai |
| 6 | gemini-3-pro-preview | 60 | 📉 | google |
| 7 | claude-sonnet-4-20250514 | 58 | ➡️ | anthropic |
| 8 | kimi-latest | 58 | ➡️ | kimi |
| 9 | claude-opus-4-6 | 58 | ➡️ | anthropic |
| 10 | claude-sonnet-4-6 | 57 | 📈 | anthropic |
| 11 | gpt-5.3-codex | 57 | ➡️ | openai |
| 12 | claude-opus-4-5-20251101 | 53 | 📉 | anthropic |
| 13 | grok-4-latest | 48 | 📈 | xai |
| 14 | claude-opus-4-7 | 47 | 📉 | anthropic |
| 15 | grok-4-0709 | 44 | 📉 | xai |
| 16 | gemini-2.5-flash | 43 | ➡️ | google |
| 17 | glm-4.6 | 39 | ➡️ | glm |
| 18 | kimi-thinking-preview | 39 | ➡️ | kimi |
| 19 | glm-4.7 | 39 | ➡️ | glm |
| 20 | gpt-5.4 | 39 | 📉 | openai |
| 21 | kimi-k2-0905-preview | 37 | ➡️ | kimi |
| 22 | kimi-k2-turbo-preview | 37 | ➡️ | kimi |
| 23 | deepseek-reasoner | 36 | ➡️ | deepseek |
| 24 | grok-code-fast-1 | 35 | 📉 | xai |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
