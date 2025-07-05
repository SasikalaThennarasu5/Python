# Project 19: Simple Discount Engine
print("\\nProject 19: Simple Discount Engine")
price = 2500
if price > 2000:
    discount = 0.2
elif price > 1000:
    discount = 0.1
else:
    discount = 0
final = price - (price * discount)
print(f"Final price: ₹{final}")
