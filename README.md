# 🎮 Free Games Tracker

Automatically tracks free games from **Epic Games** — updated daily via GitHub Actions.

_Last updated: 2026-11-14 08:24 UTC_

## 🔥 Current free games

_No free games found right now. Check back later!_

## 📦 Data

- [`data/games.json`](data/games.json) — current free games
- [`data/history.json`](data/history.json) — all games ever tracked

## 🤖 How it works

GitHub Actions runs every day at 09:00 WIB, scrapes Epic Games API,
updates the data files, and commits the changes automatically.

Built with Python + Streamlit. View the live app: _https://free-games-tracker.streamlit.app/_