# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-10-19 07:10 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Agent A: A puzzle in disguise](https://store.epicgames.com/en-US/p/agent-a-a-puzzle-in-disguise-42fe5f) | IDR 137,999 | Oct 22, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_