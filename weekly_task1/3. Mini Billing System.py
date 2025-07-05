# Project 3: Mini Billing System
print("\\nProject 3: Mini Billing System")
products = {"pen": 10, "book": 100, "bag": 500, "shoes": 700}
cart = ["pen", "book", "bag"]
total = sum(products[item] for item in cart)
if total > 1000:
    total *= 0.9
print(f"Total Bill: ₹{total}")