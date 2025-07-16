# 4. Daily Expense Tracker

expenses = {
    "2025-07-01": {"food": 250, "transport": 100, "misc": 50},
    "2025-07-02": {"food": 180, "transport": 90, "misc": 40}
}

# Daily total
for date, categories in expenses.items():
    print(f"{date} Total: {sum(categories.values())}")

# Monthly total
monthly_total = sum(sum(cat.values()) for cat in expenses.values())
print("Monthly Total:", monthly_total)

# Highest spending
highest_day = max(expenses.items(), key=lambda x: sum(x[1].values()))
print("Highest Spend:", highest_day[0])

# Copy for new month
new_month = expenses.copy()

# Food > 200
high_food_days = {d: v for d, v in expenses.items() if v.get("food", 0) > 200}
print(high_food_days)