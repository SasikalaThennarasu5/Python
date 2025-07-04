#  4. Simple ATM Simulation
balance = float(input("Enter initial balance: "))
action = input("Do you want to deposit or withdraw? ").lower()
amount = float(input("Enter amount: "))
if action == "deposit":
    balance += amount
    print(f"Deposited ₹{amount}. New balance: ₹{balance}")
elif action == "withdraw":
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
    else:
        print("Insufficient balance.")