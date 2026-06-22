# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-06-22 07:14 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Citizen Sleeper](https://store.epicgames.com/en-US/p/citizen-sleeper-944858) | IDR 137,999 | Jun 25, 2026 |
| [ROBOBEAT](https://store.epicgames.com/en-US/p/robobeat-5f084b) | IDR 108,999 | Jun 25, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_