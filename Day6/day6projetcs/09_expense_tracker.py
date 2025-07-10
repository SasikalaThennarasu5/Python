# Expense Tracker
def track_expenses(*expenses):
    total = sum(expenses)
    with_gst = list(map(lambda x: x * 1.18, expenses))
    return total, with_gst

total, updated = track_expenses(100, 200, 150)
print("Total:", total)
print("With GST:", updated)
