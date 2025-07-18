from restaurant import offers

TAX_RATE = 0.05  # 5%

def calculate_bill(items):
    subtotal = sum(item["total"] for item in items)
    tax = subtotal * TAX_RATE
    discount = offers.apply_discount(subtotal)
    grand_total = subtotal + tax - discount
    return subtotal, tax, discount, grand_total
