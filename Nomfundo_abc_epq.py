skus = [
 {"sku": "BRK-100", "demand": 2000, "cost": 45},
 {"sku": "GSK-220", "demand": 1500, "cost": 30},
 {"sku": "BLT-010", "demand": 10000, "cost": 2},
 {"sku": "BRG-330", "demand": 800, "cost": 60},
 {"sku": "SEAL-500","demand": 3000, "cost": 5},
 {"sku": "MTR-700", "demand": 50, "cost": 800},
 {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
 {"sku": "CBL-900", "demand": 400, "cost": 25},
 {"sku": "NUT-015", "demand": 5000, "cost": 3},
 {"sku": "BOLT-025", "demand": 6000, "cost": 2},
]
def usage_value(demand, cost):
 return demand * cost
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

total_value = sum(item["value"] for item in skus_sorted)
running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"
for item in skus_sorted:
 item["tier"] = assign_tier(item["cum_pct"])

for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"])
    
    tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)
# code for 5.3 
def classify_inventory(skus):
    for item in skus:
        item["value"] = usage_value(item["demand"], item["cost"])

    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0

    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100

        if item["cum_pct"] <= 80:
            item["tier"] = "A"
        elif item["cum_pct"] <= 95:
            item["tier"] = "B"
        else:
            item["tier"] = "C"

    return skus_sorted
classified_skus = classify_inventory(skus)

for item in classified_skus:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])
#5.1 I added two new SKUs, NUT-015 and BOLT-025. The tier split changes because adding new inventory items changes the total inventory value and cumulative percentages. However, the highest-value items remain in Tier A, so the overall classification does not change dramatically.
#5.2 Changing the thresholds from 80% / 95% to 70% / 90% causes some items to move into different tiers. The new classification is stricter, so fewer items fall into Tier A and Tier B, while more items can fall into Tier C.