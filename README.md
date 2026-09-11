# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-09-11 06:53 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Luftrausers](https://store.epicgames.com/en-US/p/luftrausers-51e5e9) | IDR 69,999 | Sep 17, 2026 |
| [Astral Ascent](https://store.epicgames.com/en-US/p/astral-ascent-b33bc2) | IDR 206,999 | Sep 17, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_