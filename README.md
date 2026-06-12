# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-06-12 06:28 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [The Ouroboros King](https://store.epicgames.com/en-US/p/the-ouroboros-king-e1d547) | IDR 69,999 | Jun 18, 2026 |
| [Warhammer 40K Speed Freeks](https://store.epicgames.com/en-US/p/warhammer-40k-speed-freeks-12879c) | IDR 137,999 | Jun 18, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_