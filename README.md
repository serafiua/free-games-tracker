# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-08-31 07:57 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Breathedge](https://store.epicgames.com/en-US/p/breathedge) | IDR 199,000 | Sep 03, 2026 |
| [Rival Stars Horse Racing : Desktop Edition](https://store.epicgames.com/en-US/p/rival-stars-horse-racing-dd09de) | IDR 172,999 | Sep 03, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_