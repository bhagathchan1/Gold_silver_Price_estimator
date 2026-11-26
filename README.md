# Telangana Gold and Silver Estimator

A single-page tool that estimates the price of gold or silver jewellery in Hyderabad, Karimnagar (and Chennai for comparison) from purity, weight, wastage, making charge and GST.

**Live site:** https://bhagathchan1.github.io/Gold_silver_Price_estimator/

## How to run it

**Option 1: just open the live site** (link above). Nothing to install.

**Option 2: run locally**
```bash
git clone https://github.com/bhagathchan1/Gold_silver_Price_estimator.git
cd Gold_silver_Price_estimator
open index.html            # macOS; on Linux use xdg-open, on Windows use start
```
Or serve it on http://localhost:8000:
```bash
python3 -m http.server 8000
```

**Option 3: host your own copy**: fork this repo, then go to Settings → Pages, choose branch `main` and folder `/ (root)`, and save.

## How to use it
1. Pick Gold or Silver, then a city.
2. Enter the per-gram rate your jeweller quotes.
3. Choose purity, weight, wastage % and making charge %.
4. Read the total and the breakdown on the right.

## Model

```
G = weight × rate × purity      (metal value; gold purity = K/24, silver = fineness/999)
W = G × wastage%
M = G × making%
T = 0.03 × (G + W) + 0.05 × M   (GST: 3% on metal, 5% on job work)
Price = G + W + M + T
```

Rates are editable starting values, not live quotes. Confirm against your jeweller's invoice.
