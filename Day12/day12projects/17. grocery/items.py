# grocery/items.py

GROCERY_ITEMS = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40,
    "eggs": 60,
    "rice": 70,
    "oil": 120,
    "sugar": 45
}

def list_items():
    print("Available Grocery Items:")
    for item, price in GROCERY_ITEMS.items():
        print(f"- {item.capitalize()}: ₹{price}")
