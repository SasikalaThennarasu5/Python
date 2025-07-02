# 3. Grocery List

item1 = input("Enter grocery item 1: ")
item2 = input("Enter grocery item 2: ")
item3 = input("Enter grocery item 3: ")

grocery_list = [item1, item2, item3]

print("\n🛒 Your Grocery List:")
print(*grocery_list, sep=", ")
print("Type of grocery_list:", type(grocery_list))
