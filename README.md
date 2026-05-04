# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-05-04 05:29 UTC_

## 🔥 Current free games

| Game | Normal Price | Available Until |
|------|-------------|-----------------|
| [Firestone Online Idle RPG](https://store.epicgames.com/en-US/p/firestone-online-idle-rpg-bfd04b) | 0 | May 07, 2026 |
| [Oddsparks: An Automation Adventure](https://store.epicgames.com/en-US/p/oddsparks-58440c) | IDR 269,000 | May 07, 2026 |

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_