# Grocery List Manager
inventory = []

def add_items(**kwargs):
    global inventory
    inventory = sorted(kwargs.keys())
    return sum(kwargs.values())

total = add_items(apples=2, bananas=3, milk=1)
print("Inventory:", inventory)
print("Total items:", total)
