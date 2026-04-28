import json
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Free Games Tracker",
    page_icon="🎮",
    layout="wide",
)

GAMES_FILE = Path("data/games.json")
HISTORY_FILE = Path("data/history.json")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }

.game-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 16px;
    display: flex;
    gap: 16px;
    align-items: flex-start;
    transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.game-card:hover {
    background: rgba(255,255,255,0.08);
    transform: translateY(-2px);
}
.game-thumb {
    width: 110px;
    min-width: 110px;
    height: 80px;
    object-fit: cover;
    border-radius: 10px;
}
.game-thumb-placeholder {
    width: 110px;
    min-width: 110px;
    height: 80px;
    border-radius: 10px;
    background: rgba(255,255,255,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
}
.game-info { flex: 1; min-width: 0; }
.game-title {
    font-size: 15px;
    font-weight: 600;
    margin: 0 0 6px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.game-meta { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; }
.badge-platform { font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; color: white; }
.badge-free { font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; background: #14532d; color: #86efac; }
.game-price { font-size: 13px; margin: 0 0 4px; opacity: 0.85; }
.game-price s { opacity: 0.5; }
.game-price .free-label { color: #4ade80; font-weight: 700; }
.game-until { font-size: 12px; opacity: 0.5; margin: 0 0 10px; }
.claim-btn {
    display: inline-block;
    font-size: 12px;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 8px;
    background: #0078f2;
    color: white !important;
    text-decoration: none !important;
    transition: background 0.15s;
}
.claim-btn:hover { background: #005dc4; }
.section-header { font-size: 20px; font-weight: 700; margin: 8px 0 16px; }
.section-count { font-size: 14px; font-weight: 400; opacity: 0.5; }
.empty-state { text-align: center; padding: 48px 0; opacity: 0.5; font-size: 15px; }
</style>
""", unsafe_allow_html=True)


def load_games(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path) as f:
        return json.load(f)


def format_date(iso: str) -> str:
    if not iso:
        return ""
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return dt.strftime("%d %b %Y")
    except Exception:
        return iso


PLATFORM_COLORS = {
    "Epic Games": "#0078f2",
}


def render_game_card(game: dict, is_current: bool = True):
    title = game.get("title", "Unknown")
    platform = game.get("platform", "")
    price = game.get("original_price", "Free")
    thumbnail = game.get("thumbnail", "")
    url = game.get("url", "#")
    end_date = format_date(game.get("end_date", ""))

    color = PLATFORM_COLORS.get(platform, "#888")

    if is_current and price not in ("Free", "IDR 0", ""):
        price_html = f'<s>{price}</s> <span class="free-label">FREE</span>'
    else:
        price_html = f'<span style="font-weight:600">{price}</span>'

    until_html = f'<p class="game-until">Until {end_date}</p>' if end_date else '<p class="game-until">Limited time</p>' if is_current else ''

    free_badge = '<span class="badge-free">FREE NOW</span>' if is_current else ''

    thumb_html = (
        f'<img class="game-thumb" src="{thumbnail}">'
        if thumbnail else
        '<div class="game-thumb-placeholder">🎮</div>'
    )

    card_html = f'<div class="game-card">{thumb_html}<div class="game-info"><p class="game-title" title="{title}">{title}</p><div class="game-meta"><span class="badge-platform" style="background:{color}">{platform}</span>{free_badge}</div><p class="game-price">{price_html}</p>{until_html}<a class="claim-btn" href="{url}" target="_blank">Claim now →</a></div></div>'
    st.markdown(card_html, unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("# 🎮 Free Games Tracker")
st.caption("Updated daily via GitHub Actions · Epic Games")

games = load_games(GAMES_FILE)
history = load_games(HISTORY_FILE)

# ── Stats ─────────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
col1.metric("Free right now", len(games))
col2.metric("Total tracked", len(history))

st.markdown("---")

# ── Sidebar filters ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔍 Filter")

    all_platforms = sorted({g["platform"] for g in games}) if games else ["Epic Games", "GOG"]
    selected_platforms = st.multiselect(
        "Platform",
        options=all_platforms,
        default=all_platforms,
    )

    price_options = ["All", "Under 100K", "100K–500K", "Over 500K"]
    price_filter = st.selectbox("Normal price (IDR)", price_options)

    st.markdown("---")
    show_history = st.checkbox("Show all-time history", value=False)

# ── Filter logic ──────────────────────────────────────────────────────────────
source = history if show_history else games
filtered = [g for g in source if g.get("platform") in selected_platforms]


def parse_price(g: dict) -> float:
    try:
        price = g.get("original_price", "0")
        price = price.replace("IDR", "").replace(",", "").replace("$", "").strip()
        return float(price)
    except Exception:
        return 0.0


if price_filter == "Under 100K":
    filtered = [g for g in filtered if parse_price(g) < 100000]
elif price_filter == "100K–500K":
    filtered = [g for g in filtered if 100000 <= parse_price(g) <= 500000]
elif price_filter == "Over 500K":
    filtered = [g for g in filtered if parse_price(g) > 500000]

# ── Game list ─────────────────────────────────────────────────────────────────
section_title = "📜 All-time history" if show_history else "🔥 Free right now"
count = len(filtered)
st.markdown(f'<p class="section-header">{section_title} <span class="section-count">({count} games)</span></p>', unsafe_allow_html=True)

if not filtered:
    st.markdown('<div class="empty-state">😔 No games match your filters.<br>Try adjusting them or check back tomorrow!</div>', unsafe_allow_html=True)
else:
    cols = st.columns(2)
    for i, game in enumerate(filtered):
        with cols[i % 2]:
            render_game_card(game, is_current=not show_history)