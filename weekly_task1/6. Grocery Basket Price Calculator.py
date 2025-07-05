# Project 6: Grocery Basket Price Calculator
print("\\nProject 6: Grocery Basket Price Calculator")
items = {"milk": 50, "rice": 60, "bread": 40, "oil": 100, "eggs": 60, "fruits": 120}
basket = ["milk", "rice", "bread", "oil", "eggs", "fruits"]
total = sum(items[i] for i in basket)
if len(basket) > 5:
    total -= 50
print(f"Basket Total: ₹{total}")