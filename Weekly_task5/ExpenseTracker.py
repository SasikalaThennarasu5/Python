# Expense Tracker

import json
from datetime import datetime
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self, file_path='expenses.json'):
        self.file_path = file_path
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category, note=""):
        entry = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().strftime('%Y-%m-%d')
        }
        self.expenses.append(entry)

    def get_monthly_total(self, month=None):
        if not month:
            month = datetime.now().strftime('%Y-%m')
        return sum(e['amount'] for e in self.expenses if e['date'].startswith(month))

    def generate_report(self, month=None):
        if not month:
            month = datetime.now().strftime('%Y-%m')
        report = {}
        for e in self.expenses:
            if e['date'].startswith(month):
                report[e['category']] = report.get(e['category'], 0) + e['amount']
        return report

    def visualize_expenses(self, month=None):
        report = self.generate_report(month)
        if not report:
            print("No expenses to show.")
            return
        categories = list(report.keys())
        amounts = list(report.values())
        plt.bar(categories, amounts, color='skyblue')
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.title(f"Expense Report for {month or datetime.now().strftime('%Y-%m')}")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    def export_to_file(self, filename='expenses_export.json'):
        with open(filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def save_expenses(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def load_expenses(self):
        try:
            with open(self.file_path, 'r') as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

# CLI for demo
if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense\n2. Monthly Total\n3. Generate Report\n4. Visualize Chart\n5. Export Data\n6. Save & Exit")
        choice = input("Choose: ")

        if choice == '1':
            amt = float(input("Amount: "))
            cat = input("Category (e.g. Food, Transport, Rent): ")
            note = input("Note (optional): ")
            tracker.add_expense(amt, cat, note)
        elif choice == '2':
            month = input("Enter month (YYYY-MM) or leave blank for current: ") or None
            total = tracker.get_monthly_total(month)
            print(f"Total expenses: ₹{total:.2f}")
        elif choice == '3':
            month = input("Month (YYYY-MM) or leave blank: ") or None
            report = tracker.generate_report(month)
            for cat, amt in report.items():
                print(f"{cat}: ₹{amt:.2f}")
        elif choice == '4':
            month = input("Month (YYYY-MM) or leave blank: ") or None
            tracker.visualize_expenses(month)
        elif choice == '5':
            tracker.export_to_file()
            print("Exported to expenses_export.json")
        elif choice == '6':
            tracker.save_expenses()
            print("Saved. Exiting.")
            break
