# grocery/cart.py

from grocery.items import GROCERY_ITEMS

cart = {}

def add_to_cart(item, quantity):
    if item in GROCERY_ITEMS:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} x {item} added to cart.")
    else:
        print("Item not found!")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return

    print("\nYour Cart:")
    total = 0
    for item, qty in cart.items():
        price = GROCERY_ITEMS[item] * qty
        total += price
        print(f"- {item.capitalize()} x {qty} = ₹{price}")
    print(f"Total: ₹{total}")
