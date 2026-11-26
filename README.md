# Telangana Gold and Silver Estimator

A single-page tool that estimates the price of gold or silver jewellery in Hyderabad, Karimnagar (and Chennai for comparison) from purity, weight, wastage, making charge and GST.

Open `index.html` in a browser. There is no build step or server.

## Model

```
G = weight × rate × purity      (metal value; gold purity = K/24, silver = fineness/999)
W = G × wastage%
M = G × making%
T = 0.03 × (G + W) + 0.05 × M   (GST: 3% on metal, 5% on job work)
Price = G + W + M + T
```

Rates are editable starting values, not live quotes. Confirm against your jeweller's invoice.
