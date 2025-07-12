balance = 0
transactions = []

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    balance += amount
    transactions.append(f"Deposited ${amount}")

def withdraw():
    global balance
    amount = float(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrew ${amount}")
    else:
        print("Insufficient balance.")

def check_balance():
    print(f"Current balance: ${balance}")

def show_history():
    print("Transaction History:")
    for t in transactions:
        print("-", t)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. History\n5. Exit")
    ch = input("Choose: ")
    if ch == '1': deposit()
    elif ch == '2': withdraw()
    elif ch == '3': check_balance()
    elif ch == '4': show_history()
    elif ch == '5': break
    else: print("Invalid")