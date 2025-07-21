
from validator import *
from collections import defaultdict

expenses = []

def add_expense(date, category, amount):
    expenses.append((date, category, amount))

def group_by_category():
    grouped = defaultdict(float)
    for date, cat, amt in expenses:
        grouped[cat] += amt
    return grouped

def unique_categories():
    return set(cat for _, cat, _ in expenses)

def monthly_summary(month):
    print(f"\nSummary for {month}:")
    total = 0
    for date, cat, amt in expenses:
        if date.startswith(month):
            print(f"{date} - {cat}: ₹{amt}")
            total += amt
    print(f"Total: ₹{total}")

def main():
    while True:
        print("\n1. Add 2. Group by Category 3. Categories 4. Monthly Summary 5. Exit")
        ch = input("Choose: ")

        if ch == "1":
            date = input("Date (YYYY-MM): ")
            if not is_valid_date(date): continue
            cat = input("Category: ")
            amt = input("Amount: ")
            if not is_valid_amount(amt): continue
            add_expense(date, cat, float(amt))

        elif ch == "2":
            summary = group_by_category()
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt}")

        elif ch == "3":
            print("Categories:", unique_categories())

        elif ch == "4":
            month = input("Enter month (YYYY-MM): ")
            monthly_summary(month)

        elif ch == "5":
            break

if __name__ == "__main__":
    main()
