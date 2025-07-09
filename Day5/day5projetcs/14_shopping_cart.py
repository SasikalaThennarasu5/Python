# Project 14: Shopping Cart Input App
cart = []
while True:
    item = input("Enter product (or 'done'): ")
    if item.lower() == "done":
        break
    if item.strip() == "":
        continue
    cart.append(item)
else:
    print("Products:", cart)
