# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-09-25 06:57 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Astrea Six Sided Oracles](https://store.epicgames.com/en-US/p/astrea-six-sided-oracles-33c949) | IDR 172,999 | Oct 01, 2026 |
| [Mechabellum](https://store.epicgames.com/en-US/p/mechabellum-88a843) | IDR 130,999 | Oct 01, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_