# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-10-09 08:16 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Out of Sight](https://store.epicgames.com/en-US/p/out-of-sight-b96ca8) | IDR 127,000 | Oct 15, 2026 |
| [TerraScape](https://store.epicgames.com/en-US/p/terrascape-2b12b1) | IDR 117,999 | Oct 15, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_