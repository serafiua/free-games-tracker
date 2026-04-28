import json
import os
from datetime import datetime, timezone
from pathlib import Path

from scrapers.epic import get_free_games as get_epic_games

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

GAMES_FILE = DATA_DIR / "games.json"
HISTORY_FILE = DATA_DIR / "history.json"


def load_json(path: Path) -> list:
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return []


def save_json(path: Path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def update_history(current_games: list, history: list) -> list:
    existing_keys = {(g["title"], g["platform"]) for g in history}
    for game in current_games:
        key = (game["title"], game["platform"])
        if key not in existing_keys:
            history.append(game)
            existing_keys.add(key)
    return history


def generate_readme(games: list, updated_at: str):
    lines = [
        "# 🎮 Free Games Tracker",
        "",
        "Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.",
        "",
        f"_Last updated: {updated_at} UTC_",
        "",
        "## 🔥 Current free games",
        "",
    ]

    if not games:
        lines.append("_No free games found right now. Check back later!_")
    else:
        lines.append("| Game | Normal Price | Available Until |")
        lines.append("|------|-------------|-----------------|")
        for g in games:
            end = g.get("end_date", "")
            if end:
                try:
                    end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
                    end = end_dt.strftime("%b %d, %Y")
                except Exception:
                    pass
            else:
                end = "Limited"
            price = g.get("original_price", "-")
            title = g.get("title", "-")
            url = g.get("url", "")
            title_link = f"[{title}]({url})" if url else title
            lines.append(f"| {title_link} | {price} | {end} |")

    lines += [
        "",
        "## 📦 Data",
        "",
        "- [`data/games.json`](data/games.json) — current free games",
        "- [`data/history.json`](data/history.json) — all games ever tracked",
        "",
        "## 🤖 How it works",
        "",
        "GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,",
        "updates the data files, and commits the changes automatically.",
        "",
        "Built with Python + Streamlit.",
    ]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("README.md updated.")


def main():
    print("Scraping Epic Games...")
    epic_games = get_epic_games()
    print(f"  Found {len(epic_games)} game(s)")

    all_games = epic_games
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

    save_json(GAMES_FILE, all_games)
    print(f"Saved {len(all_games)} games to {GAMES_FILE}")

    history = load_json(HISTORY_FILE)
    history = update_history(all_games, history)
    save_json(HISTORY_FILE, history)
    print(f"History now has {len(history)} total games")

    generate_readme(all_games, now)
    print("Done!")


if __name__ == "__main__":
    main()