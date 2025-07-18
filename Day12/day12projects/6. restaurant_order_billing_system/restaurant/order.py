import random
from restaurant import menu

class Order:
    def __init__(self):
        self.order_id = random.randint(1000, 9999)
        self.items = []

    def add_item(self, item_id, quantity):
        if item_id in menu.menu_items:
            item = menu.menu_items[item_id]
            self.items.append({
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity,
                "total": item["price"] * quantity
            })
        else:
            print("Invalid item ID.")

    def get_items(self):
        return self.items

    def get_order_id(self):
        return self.order_id
