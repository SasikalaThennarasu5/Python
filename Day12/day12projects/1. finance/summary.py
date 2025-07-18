from .income import get_total_income
from .expense import get_total_expense

def show_summary():
    total_income = get_total_income()
    total_expense = get_total_expense()
    savings = total_income - total_expense

    print("\n--- Finance Summary ---")
    print(f"Total Income : ₹{total_income}")
    print(f"Total Expense: ₹{total_expense}")
    print(f"Total Savings: ₹{savings}")
    print("-----------------------")
