import os
import json
from datetime import datetime

EXPENSE_FILE = os.path.join(os.getcwd(), "expense_data.json")

def add_expense(category, amount):
    data = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            data = json.load(f)

    entry = {
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(entry)

    with open(EXPENSE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_total_expense():
    if not os.path.exists(EXPENSE_FILE):
        return 0
    with open(EXPENSE_FILE, "r") as f:
        data = json.load(f)
    return sum(entry["amount"] for entry in data)
