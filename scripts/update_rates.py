"""Fetch today's gold/silver rates per city from Groww and write rates.json.
Exits non-zero (leaving the previous rates.json untouched) if anything fails to parse."""
import json, re, sys, urllib.request, datetime

CITIES = ["Hyderabad", "Karimnagar", "Chennai"]
GOLD = "https://groww.in/gold-rates/gold-rate-today-in-{}"
SILVER = "https://groww.in/silver-rates/silver-rates-in-{}"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))

def num(s):
    return float(s.replace(",", ""))

gold, silver = {}, {}
for c in CITIES:
    slug = c.lower()
    m = re.search(r"₹\s*([\d,]+(?:\.\d+)?)\s*per gram for 24 karat", get(GOLD.format(slug)))
    n = re.search(r"silver price in %s stands at\s*₹\s*([\d,]+(?:\.\d+)?)\s*per gram" % c, get(SILVER.format(slug)))
    if not m or not n:
        sys.exit(f"parse failed for {c}: gold={bool(m)} silver={bool(n)}")
    gold[c], silver[c] = num(m.group(1)), num(n.group(1))
    if not (3000 < gold[c] < 60000 and 30 < silver[c] < 1500):
        sys.exit(f"out of range for {c}: {gold[c]} {silver[c]}")

out = {
    "gold24": gold, "silver999": silver,
    "goldSource": GOLD, "silverSource": SILVER,
    "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
}
json.dump(out, open("rates.json", "w"), indent=2)
print(out)
