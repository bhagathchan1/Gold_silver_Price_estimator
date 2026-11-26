"""Fetch today's Hyderabad gold/silver rates from Groww and write rates.json."""
import json, re, sys, urllib.request, datetime

GOLD = "https://groww.in/gold-rates/gold-rate-today-in-hyderabad"
SILVER = "https://groww.in/silver-rates/silver-rates-in-hyderabad"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return re.sub(r"<[^>]+>", " ", urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore"))

def money(s):
    return float(s.replace(",", ""))

g = get(GOLD)
m = re.search(r"₹\s*([\d,]+(?:\.\d+)?)\s*per gram for 24 karat", g)
gold24 = money(m.group(1)) if m else None
s = get(SILVER)
m = re.search(r"silver price in Hyderabad stands at\s*₹\s*([\d,]+(?:\.\d+)?)\s*per gram", s)
silver999 = money(m.group(1)) if m else None

# Sanity check so a page redesign can't publish garbage.
if not gold24 or not silver999 or not (3000 < gold24 < 60000) or not (30 < silver999 < 1500):
    sys.exit(f"parse failed or out of range: gold={gold24} silver={silver999}")

out = {
    "gold24": gold24, "silver999": silver999,
    "goldSource": GOLD, "silverSource": SILVER,
    "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
}
json.dump(out, open("rates.json", "w"), indent=2)
print(out)
