# Project 9: Simple Shopping Cart
print("\\nProject 9: Simple Shopping Cart")
store = {"soap": 30, "brush": 20, "paste": 50}
chosen = ["soap", "brush", "paste"]
total = sum(store[i] for i in chosen)
print(f"Total Bill: ₹{total}")
