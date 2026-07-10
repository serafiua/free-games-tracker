# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-07-10 05:57 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Nova Lands](https://store.epicgames.com/en-US/p/nova-lands-4d1788) | IDR 165,999 | Jul 16, 2026 |
| [Tattoo Tycoon](https://store.epicgames.com/en-US/p/tattoo-tycoon-b4352c) | IDR 269,000 | Jul 16, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_