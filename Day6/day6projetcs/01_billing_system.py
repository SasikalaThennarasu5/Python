# Billing System
total = 0

def add_items(*prices):
    global total
    total += sum(prices)
    return total

def apply_discount(amount):
    return amount * 0.9  # 10% discount

print("Total before discount:", add_items(100, 200, 50))
print("Total after discount:", apply_discount(total))
