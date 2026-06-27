# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-06-27 05:48 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [RollerCoaster Tycoon 3 Complete Edition](https://store.epicgames.com/en-US/p/rollercoaster-tycoon-3-complete-edition) | IDR 288,000 | Jul 02, 2026 |
| [Voidwrought](https://store.epicgames.com/en-US/p/voidwrought-ce8f4b) | IDR 137,999 | Jul 02, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_