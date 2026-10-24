# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-10-24 06:44 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Sker Ritual](https://store.epicgames.com/en-US/p/sker-ritual-aac702) | IDR 172,999 | Oct 29, 2026 |
| [Home - A Unique Horror Adventure](https://store.epicgames.com/en-US/p/home-19212a) | IDR 34,999 | Oct 29, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_