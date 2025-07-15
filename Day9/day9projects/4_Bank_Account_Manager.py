# Project 4: Bank Account Manager
customers = [
    (101, "Alice", (5000, "Active")),
    (102, "Bob", (3000, "Inactive")),
    (103, "Charlie", (7000, "Active"))
]

for acc_no, name, (balance, status) in customers:
    print(f"Account: {acc_no}, Name: {name}, Balance: {balance}, Status: {status}")