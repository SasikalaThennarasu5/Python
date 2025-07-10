# Electricity Bill Calculator
def calculate_bill(*units):
    total = 0
    for unit in units:
        if unit <= 100:
            total += unit * 2
        elif unit <= 300:
            total += 100 * 2 + (unit - 100) * 5
        else:
            total += 100 * 2 + 200 * 5 + (unit - 300) * 8
    gst = lambda x: x * 1.18
    return gst(total)

print("Total Bill with GST:", calculate_bill(120, 150))
