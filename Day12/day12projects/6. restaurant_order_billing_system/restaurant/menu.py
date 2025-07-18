menu_items = {
    1: {"name": "Burger", "price": 120},
    2: {"name": "Pizza", "price": 250},
    3: {"name": "Pasta", "price": 180},
    4: {"name": "Coke", "price": 50},
    5: {"name": "Ice Cream", "price": 90},
}

def display_menu():
    print("\n--- MENU ---")
    for item_id, item in menu_items.items():
        print(f"{item_id}. {item['name']:15} ₹{item['price']}")
