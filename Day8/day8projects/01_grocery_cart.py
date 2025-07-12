# Grocery Cart System

cart = []

# Add items
cart.append("Apple")
cart.extend(["Banana", "Milk", "Bread", "Eggs", "Butter", "Milk"])  # Duplicate added

# Display items
print("Items in cart:")
for item in cart:
    print("-", item)

# Remove item
cart.remove("Bread")  # Removes first occurrence

# Total count
print(f"\nTotal items: {len(cart)}")

# Check duplicates
for item in set(cart):
    if cart.count(item) > 1:
        print(f"Duplicate found: {item} ({cart.count(item)} times)")

# First 3 items
print("\nTop 3 items:", cart[:3])
