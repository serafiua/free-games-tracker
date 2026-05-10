# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-05-10 05:32 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Arranger: A Role-Puzzling Adventure](https://store.epicgames.com/en-US/p/arranger-a-rolepuzzling-adventure-dbfde7) | IDR 169,000 | May 14, 2026 |
| [Trash Goblin](https://store.epicgames.com/en-US/p/trash-goblin-cd5fd7) | IDR 137,999 | May 14, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_