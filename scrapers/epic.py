import requests
from datetime import datetime, timezone


EPIC_API = (
    "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
    "?locale=en-US&country=ID&allowCountries=ID"
)


def is_free_via_promotion(item: dict, now: datetime):
    promotions = item.get("promotions") or {}
    offers = promotions.get("promotionalOffers", [])
    for promo_group in offers:
        for offer in promo_group.get("promotionalOffers", []):
            if offer.get("discountSetting", {}).get("discountPercentage", 100) == 0:
                end_raw = offer.get("endDate", "")
                if end_raw:
                    try:
                        end_dt = datetime.fromisoformat(end_raw.replace("Z", "+00:00"))
                        if end_dt < now:
                            continue
                    except Exception:
                        pass
                return True, offer
    return False, None


def get_price(item: dict) -> str:
    try:
        fmt = item["price"]["totalPrice"]["fmtPrice"]["originalPrice"]
        fmt = fmt.replace("\u00a0", " ").replace(".00", "")
        return fmt
    except Exception:
        pass
    try:
        raw = item["price"]["totalPrice"]["originalPrice"]
        if raw > 0:
            return f"IDR {raw / 100:,.0f}"
    except Exception:
        pass
    return "Free"


def get_free_games() -> list[dict]:
    try:
        resp = requests.get(EPIC_API, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[Epic] Request failed: {e}")
        return []

    elements = (
        data.get("data", {})
        .get("Catalog", {})
        .get("searchStore", {})
        .get("elements", [])
    )

    games = []
    now = datetime.now(timezone.utc)

    for item in elements:
        is_promo, active_offer = is_free_via_promotion(item, now)

        if not is_promo:
            continue

        price_str = get_price(item)

        # Thumbnail
        images = item.get("keyImages", [])
        thumbnail = ""
        for img in images:
            if img.get("type") in ("Thumbnail", "OfferImageWide", "DieselStoreFrontWide"):
                thumbnail = img.get("url", "")
                break

        # URL
        product_slug = ""
        for mapping in item.get("catalogNs", {}).get("mappings", []) or []:
            if mapping.get("pageType") == "productHome":
                product_slug = mapping.get("pageSlug", "")
                break
        if not product_slug:
            slug = item.get("productSlug") or item.get("urlSlug", "")
            product_slug = slug.split("/")[0] if slug else ""

        url = (
            f"https://store.epicgames.com/en-US/p/{product_slug}"
            if product_slug
            else "https://store.epicgames.com/en-US/free-games"
        )

        games.append({
            "title": item.get("title", "Unknown"),
            "platform": "Epic Games",
            "original_price": price_str,
            "thumbnail": thumbnail,
            "url": url,
            "start_date": active_offer.get("startDate", "") if active_offer else "",
            "end_date": active_offer.get("endDate", "") if active_offer else "",
            "scraped_at": now.isoformat(),
        })

    return games