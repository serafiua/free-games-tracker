# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-05-22 06:01 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Down in Bermuda](https://store.epicgames.com/en-US/p/down-in-bermuda) | 0 | May 28, 2026 |
| [Tomb Raider I-III Remastered Starring Lara Croft](https://store.epicgames.com/en-US/p/tomb-raider-iiii-remastered-538640) | 0 | May 28, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_