# AI Stupid Level Tracker

> Auto-updated: 2026-05-01 07:18:18 (UTC)

Data source: [aistupidlevel.info](https://aistupidlevel.info/)

| Rank | Model | Score | Trend | Provider |
|------|-------|-------|-------|----------|
| 1 | gemini-3-pro-preview | 68 | ➡️ | google |
| 2 | claude-opus-4-5-20251101 | 65 | ➡️ | anthropic |
| 3 | claude-sonnet-4-5-20250929 | 64 | ➡️ | anthropic |
| 4 | claude-sonnet-4-20250514 | 63 | 📈 | anthropic |
| 5 | deepseek-reasoner | 63 | 📈 | deepseek |
| 6 | deepseek-chat | 63 | ➡️ | deepseek |
| 7 | claude-sonnet-4-6 | 63 | ➡️ | anthropic |
| 8 | claude-opus-4-1-20250805 | 62 | ➡️ | anthropic |
| 9 | gpt-5.2 | 62 | ➡️ | openai |
| 10 | claude-opus-4-7 | 62 | ➡️ | anthropic |
| 11 | gpt-5.5 | 62 | ➡️ | openai |
| 12 | kimi-latest | 60 | ➡️ | kimi |
| 13 | kimi-k2-turbo-preview | 60 | 📈 | kimi |
| 14 | claude-opus-4-6 | 60 | ➡️ | anthropic |
| 15 | gpt-5.3-codex | 59 | ➡️ | openai |
| 16 | gemini-2.5-flash | 53 | 📈 | google |
| 17 | grok-code-fast-1 | 49 | ➡️ | xai |
| 18 | kimi-k2-0905-preview | 45 | 📈 | kimi |
| 19 | grok-4-latest | 44 | 📉 | xai |
| 20 | grok-4-0709 | 44 | 📈 | xai |
| 21 | gpt-5.4 | 42 | 📉 | openai |
| 22 | glm-4.6 | 40 | ➡️ | glm |
| 23 | kimi-thinking-preview | 40 | ➡️ | kimi |
| 24 | glm-4.7 | 40 | ➡️ | glm |

Total: 24 models

---

## How it works

GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the [aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), and commits the results back to this repo.

- `data/latest.json` — latest full API response
- `data/history.csv` — append-only history for trend analysis
