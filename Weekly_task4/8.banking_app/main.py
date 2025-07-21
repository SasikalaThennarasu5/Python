from auth import login

users = {"alice": {"balance": 1000, "transactions": []}}

def deposit(user, amount):
    users[user]["balance"] += amount
    users[user]["transactions"].append(("deposit", amount))

def withdraw(user, amount):
    if users[user]["balance"] >= amount:
        users[user]["balance"] -= amount
        users[user]["transactions"].append(("withdraw", amount))
    else:
        print("Insufficient funds")

user = "alice"
if login(user, users):
    deposit(user, 200)
    withdraw(user, 100)
    print(users[user])