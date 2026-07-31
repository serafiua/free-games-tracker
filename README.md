# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-07-31 05:29 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [OTXO](https://store.epicgames.com/en-US/p/otxo-396b8b) | IDR 103,999 | Aug 06, 2026 |
| [Sol Cesto](https://store.epicgames.com/en-US/p/sol-cesto-e9b803) | IDR 122,999 | Aug 06, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_