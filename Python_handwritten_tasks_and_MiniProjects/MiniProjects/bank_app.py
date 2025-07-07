# 6. Bank Withdrawal Simulator
# Scenario: A bank app wants to check balance before withdrawal

# Input: Initial balance and withdrawal amount
try:
    balance = float(input("Enter your current balance (₹): "))
    withdrawal = float(input("Enter amount to withdraw (₹): "))

    # Use if to check if sufficient balance exists
    if withdrawal <= balance:
        balance -= withdrawal  # Use variables and arithmetic

        print("\n=========== Transaction Summary ===========")
        print(f" Withdrawal Status : Successful")
        print(f" Amount Withdrawn  : ₹{withdrawal:.2f}")
        print(f" Remaining Balance : ₹{balance:.2f}")
        print("===========================================\n")

    else:
        # Use else to print error if not enough balance
        print("\n=========== Transaction Failed ============")
        print(f" Withdrawal Status : Failed - Insufficient Balance")
        print(f" Attempted Amount  : ₹{withdrawal:.2f}")
        print(f" Available Balance : ₹{balance:.2f}")
        print("===========================================\n")

except ValueError:
    print("\n Invalid input! Please enter numeric values.\n")
