#  20. E-commerce Mini Checkout System
price = float(input("Enter product price: "))
qty = int(input("Enter quantity: "))
code = input("Enter discount code (DISC10/DISC20): ").upper()
total = price * qty
if code in ["DISC10", "DISC20"]:
    discount = 10 if code == "DISC10" else 20
    total -= (total * discount / 100)
print(f"Total amount to pay: ₹{total}")
