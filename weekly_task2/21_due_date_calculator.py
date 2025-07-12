from datetime import datetime, timedelta

book = input("Enter book name: ")
borrow_date_str = input("Enter borrow date (YYYY-MM-DD): ")

try:
    borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d")
    due_date = borrow_date + timedelta(days=7)
    print(f"Book: {book}\nBorrowed on: {borrow_date.date()}\nDue on: {due_date.date()}")
except ValueError:
    print("Invalid date format.")