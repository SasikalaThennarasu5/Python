# Project 6: ATM Withdrawal Limit System
limit = 10000
withdrawn = 0
while withdrawn < limit:
    entry = input("Enter amount to withdraw (or type 'stop'): ")
    if entry.lower() == "stop":
        break
    amount = int(entry)
    if withdrawn + amount > limit:
        print("Limit exceeded")
        break
    withdrawn += amount
    print(f"Withdrawn so far: ₹{withdrawn}")
