# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-09-23 07:06 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Mindcop](https://store.epicgames.com/en-US/p/mindcop-78e6c1) | IDR 81,000 | Sep 24, 2026 |
| [Shogun Showdown](https://store.epicgames.com/en-US/p/shogun-showdown-61832d) | IDR 103,999 | Sep 24, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_