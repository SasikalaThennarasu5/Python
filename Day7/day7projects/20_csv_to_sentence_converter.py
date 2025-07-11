items = input("Enter comma-separated items: ").split(",")
items = [item.strip() for item in items]
if len(items) == 1:
    print(f"You bought {items[0]}.")
else:
    print("You bought " + ", ".join(items[:-1]) + ", and " + items[-1] + ".")