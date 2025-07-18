from .income import add_income
from .expense import add_expense
from .summary import show_summary

def run_cli():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            source = input("Income Source: ")
            amount = float(input("Amount (₹): "))
            add_income(source, amount)
            print("Income added.")

        elif choice == "2":
            category = input("Expense Category: ")
            amount = float(input("Amount (₹): "))
            add_expense(category, amount)
            print("Expense added.")

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run_cli()
