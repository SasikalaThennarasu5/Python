# 15. Shopping Cart
item1 = input("Enter item 1 name: ")
price1 = float(input("Enter price of item 1: "))
item2 = input("Enter item 2 name: ")
price2 = float(input("Enter price of item 2: "))
item3 = input("Enter item 3 name: ")
price3 = float(input("Enter price of item 3: "))
cart = {item1: price1, item2: price2, item3: price3}
total = sum(cart.values())
print("\n🛒 Shopping Cart:", cart)
print(f"Total Price: ₹{total}")
