# expensesplitter/members.py

from decimal import Decimal

group_members = []

def add_member(name):
    if name and name not in group_members:
        group_members.append(name)
        print(f"Member '{name}' added.")
    else:
        print("Invalid or duplicate member name.")

def list_members():
    print("Group Members:")
    for member in group_members:
        print(f"- {member}")
