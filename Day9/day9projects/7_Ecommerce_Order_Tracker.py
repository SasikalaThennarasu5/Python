# Project 7: E-commerce Order Tracker
orders = [
    (1, "Alice", ("Laptop", "Mouse")),
    (2, "Bob", ("Book", "Pen", "Notebook")),
    (3, "Charlie", ("Phone",))
]

for order_id, customer, items in orders:
    print(f"Order ID: {order_id}, Customer: {customer}")
    for item in items:
        print(f"  - {item}")