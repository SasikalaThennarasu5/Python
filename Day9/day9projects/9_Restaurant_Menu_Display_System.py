# Project 9: Restaurant Menu Display System
menu = [
    (1, "Burger", 100),
    (2, "Pizza", 150),
    (3, "Pasta", 120)
]

for item_id, name, price in menu:
    print(f"{item_id}. {name} - Rs.{price}")

expensive = max(menu, key=lambda x: x[2])
print("Most Expensive Item:", expensive[1])