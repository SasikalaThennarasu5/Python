import os
import json
from datetime import datetime

INCOME_FILE = os.path.join(os.getcwd(), "income_data.json")

def add_income(source, amount):
    data = []
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "r") as f:
            data = json.load(f)

    entry = {
        "source": source,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(entry)

    with open(INCOME_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_total_income():
    if not os.path.exists(INCOME_FILE):
        return 0
    with open(INCOME_FILE, "r") as f:
        data = json.load(f)
    return sum(entry["amount"] for entry in data)
