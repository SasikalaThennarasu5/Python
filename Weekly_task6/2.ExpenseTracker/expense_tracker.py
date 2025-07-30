import csv
from datetime import datetime
from functools import wraps

# ------------------ Decorator for Validation ------------------ #
def validate_input(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        amount = args[0]
        category = args[1]
        try:
            float(amount)
        except ValueError:
            print("Invalid amount format.")
            return
        if not category.strip():
            print("Category cannot be empty.")
            return
        return func(self, *args, **kwargs)
    return wrapper

# ------------------ Expense Class ------------------ #
class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = float(amount)
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {"amount": self.amount, "category": self.category, "date": self.date}

    def __str__(self):
        return f"{self.date} | {self.category:15} | ${self.amount:7.2f}"

# ------------------ Expense Tracker ------------------ #
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    @validate_input
    def add_expense(self, amount, category, date=None):
        try:
            if date:
                datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

        expense = Expense(amount, category, date)
        self.expenses.append(expense)
        print("Expense added.")

    def view_expenses_by_category(self, category):
        print(f"\nExpenses for category: {category}")
        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                print(expense)

    def view_expenses_by_month(self, month):
        print(f"\nExpenses for month: {month}")
        for expense in self.expenses:
            if datetime.strptime(expense.date, "%Y-%m-%d").strftime("%Y-%m") == month:
                print(expense)

    def filter_expenses_above(self, amount):
        print(f"\nExpenses above ${amount}:")
        for expense in self.expenses:
            if expense.amount > amount:
                print(expense)

    def get_unique_categories(self):
        return set(exp.category for exp in self.expenses)

    def expenses_in_date_range(self, start_date, end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return (exp for exp in self.expenses if start <= datetime.strptime(exp.date, "%Y-%m-%d") <= end)

    def save_to_csv(self, filename="expenses.csv"):
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["amount", "category", "date"])
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow(exp.to_dict())
        print("Expenses saved to CSV.")

# ------------------ Menu Interface ------------------ #
def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View by Category")
        print("3. View by Month")
        print("4. Filter > Amount")
        print("5. Unique Categories")
        print("6. Expenses in Date Range")
        print("7. Save to CSV")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Amount: ")
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD, optional): ")
            tracker.add_expense(amount, category, date if date else None)

        elif choice == "2":
            category = input("Enter category: ")
            tracker.view_expenses_by_category(category)

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            tracker.view_expenses_by_month(month)

        elif choice == "4":
            amt = float(input("Enter amount to filter: "))
            tracker.filter_expenses_above(amt)

        elif choice == "5":
            categories = tracker.get_unique_categories()
            print("Unique categories:", ", ".join(categories))

        elif choice == "6":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            print(f"\nExpenses between {start} and {end}:")
            for exp in tracker.expenses_in_date_range(start, end):
                print(exp)

        elif choice == "7":
            tracker.save_to_csv()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
