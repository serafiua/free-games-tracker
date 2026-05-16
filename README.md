# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-05-16 05:22 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [The Telltale Batman Shadows Edition](https://store.epicgames.com/en-US/p/the-telltale-batman) | 0 | May 21, 2026 |
| [Sunderfolk - Standard Edition](https://store.epicgames.com/en-US/p/sunderfolk-standard-edition-83c05e) | 0 | May 21, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_