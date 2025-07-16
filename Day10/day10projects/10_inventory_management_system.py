inventory = {
    "pen": {"stock": 50, "min_required": 20, "supplier": "ABC"},
    "book": {"stock": 10, "min_required": 15, "supplier": "XYZ"}
}

# Alert
alerts = {k: v for k, v in inventory.items() if v["stock"] < v["min_required"]}
print("Alerts:", alerts)

# Add new
inventory.setdefault("eraser", {"stock": 30, "min_required": 10, "supplier": "DEF"})

# Delete discontinued
inventory.pop("pen", None)

# Low stock export
low_stock = {k: v for k, v in inventory.items() if v["stock"] < 20}
print("Low Stock:", low_stock)