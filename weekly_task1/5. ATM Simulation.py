# Project 5: ATM Simulation
print("\\nProject 5: ATM Simulation")
balance = 5000
for _ in range(3):
    operation = "withdraw"
    if operation == "deposit":
        balance += 1000
    elif operation == "withdraw":
        amt = 2000
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")
    elif operation == "check":
        print(f"Balance: ₹{balance}")
print(f"Final Balance: ₹{balance}")