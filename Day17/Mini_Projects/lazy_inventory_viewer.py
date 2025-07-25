import time

# Step 1: Mock a large product inventory
mock_inventory = [
    {"id": 1, "name": "Laptop", "stock": 10},
    {"id": 2, "name": "Mouse", "stock": 0},
    {"id": 3, "name": "Keyboard", "stock": 5},
    {"id": 4, "name": "Monitor", "stock": 2},
    {"id": 5, "name": "USB Cable", "stock": 0},
    {"id": 6, "name": "Charger", "stock": 8},
    {"id": 7, "name": "Tablet", "stock": 0},
    {"id": 8, "name": "Printer", "stock": 4},
    {"id": 9, "name": "Desk Lamp", "stock": 0},
    {"id": 10, "name": "Hard Drive", "stock": 6},
]

# Step 2: Generator to yield one product at a time
def product_generator(products):
    for product in products:
        yield product
    return "End of Inventory"

# Step 3: Filter only products that are in stock using generator expression
in_stock_products = (p for p in mock_inventory if p["stock"] > 0)

# Step 4: Implement pagination: 5 per scroll
def view_inventory_paginated():
    gen = product_generator(in_stock_products)
    page_size = 5
    try:
        while True:
            print("=== Next Page ===")
            for _ in range(page_size):
                product = next(gen)
                print(f"ID: {product['id']} | {product['name']} | Stock: {product['stock']}")
            input("\nPress Enter to scroll...")
    except StopIteration as e:
        print("\n No more products to show.")
        print(f" {e.value}")

# Run it
if __name__ == "__main__":
    view_inventory_paginated()
