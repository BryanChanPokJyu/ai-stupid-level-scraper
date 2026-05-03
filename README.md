# AI Stupid Level Tracker

> Auto-updated: 2026-05-03 17:34:27 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | claude-sonnet-4-5-20250929 | 69 | ➡️ | anthropic |
| 2 | claude-opus-4-6 | 66 | 📈 | anthropic |
| 3 | gemini-3-pro-preview | 65 | ➡️ | google |
| 4 | claude-opus-4-5-20251101 | 64 | ➡️ | anthropic |
| 5 | claude-sonnet-4-6 | 64 | ➡️ | anthropic |
| 6 | deepseek-reasoner | 63 | 📈 | deepseek |
| 7 | deepseek-chat | 63 | ➡️ | deepseek |
| 8 | gpt-5.4 | 62 | ➡️ | openai |
| 9 | gpt-5.2 | 61 | ➡️ | openai |
| 10 | claude-opus-4-1-20250805 | 59 | ➡️ | anthropic |
| 11 | kimi-latest | 59 | ➡️ | kimi |
| 12 | gpt-5.5 | 59 | ➡️ | openai |
| 13 | claude-sonnet-4-20250514 | 58 | 📉 | anthropic |
| 14 | gpt-5.3-codex | 58 | ➡️ | openai |
| 15 | claude-opus-4-7 | 56 | ➡️ | anthropic |
| 16 | grok-4-latest | 47 | ➡️ | xai |
| 17 | grok-code-fast-1 | 47 | 📉 | xai |
| 18 | gemini-2.5-flash | 47 | 📈 | google |
| 19 | grok-4-0709 | 42 | ➡️ | xai |
| 20 | kimi-thinking-preview | 41 | ➡️ | kimi |
| 21 | glm-4.6 | 40 | ➡️ | glm |
| 22 | kimi-k2-turbo-preview | 40 | ➡️ | kimi |
| 23 | glm-4.7 | 40 | ➡️ | glm |
| 24 | kimi-k2-0905-preview | 39 | 📈 | kimi |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
