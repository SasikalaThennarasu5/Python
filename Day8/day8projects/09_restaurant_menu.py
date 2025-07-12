# Restaurant Menu System

menu = [["Idly", 30], ["Dosa", 40], ["Pongal", 50]]

# Add dish
menu.append(["Vada", 20])

# Remove sold out
menu = [dish for dish in menu if dish[0] != "Dosa"]

# Display
print("Menu:")
for dish, price in menu:
    print(f"{dish}: Rs.{price}")
