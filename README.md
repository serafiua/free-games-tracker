# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-08-10 03:46 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Beacon Pines](https://store.epicgames.com/en-US/p/beacon-pines-629fc3) | IDR 137,999 | Aug 13, 2026 |
| [We Were Here Together](https://store.epicgames.com/en-US/p/we-were-here-together-6a6d66) | IDR 89,999 | Aug 13, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_