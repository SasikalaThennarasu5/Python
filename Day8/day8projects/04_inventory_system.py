# Inventory System

inventory = [["Soap", 10], ["Shampoo", 5], ["Toothpaste", 15]]

# Add product
inventory.append(["Conditioner", 7])

# Update quantity
for item in inventory:
    if item[0] == "Soap":
        item[1] = 12

# Delete product
inventory = [item for item in inventory if item[0] != "Shampoo"]

# Display all items
print("Inventory:")
for name, qty in inventory:
    print(f"{name}: {qty}")
