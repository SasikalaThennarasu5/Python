
import csv
import datetime
from functools import wraps

# Decorator for validating input
def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            print(f"Input error: {ve}")
    return wrapper

# Generator: Yield expenses in a date range
def expense_generator(expenses, start_date, end_date):
    for expense in expenses:
        if start_date <= datetime.datetime.strptime(expense['date'], "%Y-%m-%d").date() <= end_date:
            yield expense

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date
        }

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    @validate_input
    def add_expense(self, amount, category, date):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")
        expense = Expense(amount, category, date)
        self.expenses.append(expense.to_dict())
        print("Expense added successfully.")

    def view_by_category(self, category):
        print(f"Expenses in category: {category}")
        for exp in self.expenses:
            if exp['category'].lower() == category.lower():
                print(f"${exp['amount']} on {exp['date']}")

    def view_by_month(self, month):
        print(f"Expenses in month: {month}")
        for exp in self.expenses:
            if datetime.datetime.strptime(exp['date'], "%Y-%m-%d").month == month:
                print(f"${exp['amount']} in {exp['category']} on {exp['date']}")

    def save_to_csv(self, filename="expenses.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['amount', 'category', 'date'])
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow(exp)
        print("Expenses saved to CSV.")

    def show_expenses_over(self, threshold):
        print(f"Expenses over ${threshold}:")
        for exp in self.expenses:
            if exp['amount'] > threshold:
                print(f"${exp['amount']} in {exp['category']} on {exp['date']}")

    def get_unique_categories(self):
        return set(exp['category'] for exp in self.expenses)

# Example Usage
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense(50, "Groceries", "2025-07-29")
    tracker.add_expense(120, "Utilities", "2025-07-15")
    tracker.add_expense(30, "Transport", "2025-07-20")

    tracker.view_by_category("Groceries")
    tracker.view_by_month(7)
    tracker.show_expenses_over(40)
    tracker.save_to_csv()

    print("Unique Categories:", tracker.get_unique_categories())

    print("Expenses between 2025-07-10 and 2025-07-31:")
    for exp in expense_generator(tracker.expenses, datetime.date(2025, 7, 10), datetime.date(2025, 7, 31)):
        print(exp)
