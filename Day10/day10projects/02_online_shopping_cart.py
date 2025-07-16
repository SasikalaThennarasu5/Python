# 2. Online Shopping Cart

cart = {
    "apple": {"quantity": 2, "price": 50},
    "banana": {"quantity": 5, "price": 10}
}

# Add item
cart["mango"] = {"quantity": 3, "price": 30}

# Update item
cart["banana"]["quantity"] = 7

# Remove item
cart.pop("apple", None)

# Total bill
total = sum(item["quantity"] * item["price"] for item in cart.values())
print("Total Bill:", total)

# Remove out-of-stock
for item in list(cart.keys()):
    if cart[item]["quantity"] == 0:
        cart.pop(item)

# Highest value item
highest = max(cart.items(), key=lambda x: x[1]["quantity"] * x[1]["price"])
print("Highest:", highest[0])