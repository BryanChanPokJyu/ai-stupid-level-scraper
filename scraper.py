#!/usr/bin/env python3
"""
定时爬取 aistupidlevel.info 各模型降智评分
GitHub Actions 定时运行，结果自动 commit 回仓库
"""

import json
import os
import csv
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

API_URL = "https://aistupidlevel.info/api/dashboard/scores"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
LATEST_FILE = os.path.join(DATA_DIR, "latest.json")
HISTORY_CSV = os.path.join(DATA_DIR, "history.csv")

HEADERS = {
    "User-Agent": "AIStupidLevel-Scraper/1.0",
    "Accept": "application/json",
}


def fetch_scores():
    req = Request(API_URL, headers=HEADERS)
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def save_latest(data):
    with open(LATEST_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def append_history(models, fetch_time):
    file_exists = os.path.exists(HISTORY_CSV)
    with open(HISTORY_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "fetch_time", "model_id", "name", "provider",
                "score", "trend", "status", "confidence_lower",
                "confidence_upper", "standard_error", "last_updated"
            ])
        for m in models:
            writer.writerow([
                fetch_time,
                m.get("id", ""),
                m.get("name", ""),
                m.get("provider", ""),
                m.get("currentScore", ""),
                m.get("trend", ""),
                m.get("status", ""),
                m.get("confidenceLower", ""),
                m.get("confidenceUpper", ""),
                m.get("standardError", ""),
                m.get("lastUpdated", ""),
            ])


def generate_readme(models, fetch_time):
    sorted_models = sorted(models, key=lambda x: x.get("currentScore", 0), reverse=True)
    lines = [
        "# AI Stupid Level Tracker",
        "",
        f"> Auto-updated: {fetch_time} (UTC)",
        "",
        "Data source: [aistupidlevel.info](https://aistupidlevel.info/)",
        "",
        "| Rank | Model | Score | Trend | Provider |",
        "|------|-------|-------|-------|----------|",
    ]
    trend_map = {"up": "📈", "down": "📉", "stable": "➡️"}
    for i, m in enumerate(sorted_models, 1):
        trend = trend_map.get(m.get("trend", ""), "❓")
        lines.append(f"| {i} | {m['name']} | {m['currentScore']} | {trend} | {m['provider']} |")

    lines += [
        "",
        f"Total: {len(models)} models",
        "",
        "---",
        "",
        "## How it works",
        "",
        "GitHub Actions runs `scraper.py` every hour via cron, fetches scores from the "
        "[aistupidlevel.info API](https://aistupidlevel.info/api/dashboard/scores), "
        "and commits the results back to this repo.",
        "",
        "- `data/latest.json` — latest full API response",
        "- `data/history.csv` — append-only history for trend analysis",
    ]
    readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    fetch_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{fetch_time}] Fetching aistupidlevel.info ...")

    try:
        raw = fetch_scores()
    except (URLError, HTTPError) as e:
        print(f"[ERROR] Request failed: {e}")
        raise

    if not raw.get("success"):
        raise RuntimeError(f"API returned failure: {raw}")

    models = raw.get("data", [])
    if not models:
        raise RuntimeError("No model data returned")

    os.makedirs(DATA_DIR, exist_ok=True)
    save_latest(raw)
    append_history(models, fetch_time)
    generate_readme(models, fetch_time)

    sorted_models = sorted(models, key=lambda x: x.get("currentScore", 0), reverse=True)
    for i, m in enumerate(sorted_models, 1):
        print(f"  {i:>2}. {m['name']:<35} {m['currentScore']:>3}  {m.get('trend', '')}")

    print(f"\nDone. {len(models)} models saved.")


if __name__ == "__main__":
    main()
