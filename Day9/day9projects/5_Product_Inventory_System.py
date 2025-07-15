# Project 5: Product Inventory System
products = [
    (1, "Pen", 10.0, True),
    (2, "Notebook", 50.0, False),
    (3, "Eraser", 5.0, True)
]

total_value = sum(price for _, _, price, in_stock in products if in_stock)
print(f"Total Inventory Value: {total_value}")

sorted_products = sorted(products, key=lambda x: x[2])
for pid, name, price, in_stock in sorted_products:
    print(f"{name}: Rs.{price}, In stock: {in_stock}")