# Project 11: Meal Ordering System
orders = []
while True:
    item = input("Enter item (or 'done'): ")
    if item.lower() == "done":
        break
    if item.strip() == "":
        continue
    orders.append(item)
else:
    print("Total items:", len(orders))
print("Ordered:", orders)
