# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-07-06 06:21 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [River City Girls 2](https://store.epicgames.com/en-US/p/river-city-girls-2-77af3a) | IDR 276,999 | Jul 09, 2026 |
| [I Have No Mouth, and I Must Scream](https://store.epicgames.com/en-US/p/i-have-no-mouth-and-i-must-scream-95c5c2) | IDR 69,999 | Jul 09, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_