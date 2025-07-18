# expensesplitter/report.py

import csv
from decimal import Decimal
from expensesplitter.split import expenses
from expensesplitter.members import group_members

def show_report():
    balances = {member: Decimal('0.00') for member in group_members}

    for entry in expenses:
        for member, value in entry["split"].items():
            balances[member] += value

    print("\n--- Balance Report ---")
    for member, balance in balances.items():
        status = "gets back" if balance > 0 else "owes"
        print(f"{member}: {status} ₹{abs(balance):.2f}")

def export_report(filename="expense_report.csv"):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Payer", "Amount", "Reason", "Split (Member: Amount)"])
        for entry in expenses:
            split_str = ", ".join(f"{m}: ₹{v:.2f}" for m, v in entry["split"].items())
            writer.writerow([entry["payer"], f"₹{entry['amount']}", entry["reason"], split_str])
    print(f"✅ Report exported to '{filename}'.")
