def atm_simulation():
    balance = 1000
    history = []
    attempts = 3
    pin = "1234"

    while attempts > 0:
        user_pin = input("Enter PIN: ")
        if user_pin == pin:
            while True:
                print("\n1. Balance Inquiry\n2. Deposit\n3. Withdraw\n4. Transaction History\n5. Exit")
                choice = input("Choose an option: ")
                if choice == '1':
                    print(f"Balance: ${balance}")
                elif choice == '2':
                    try:
                        amount = float(input("Enter deposit amount: "))
                        balance += amount
                        history.append(f"Deposited ${amount}")
                    except ValueError:
                        print("Invalid amount.")
                elif choice == '3':
                    try:
                        amount = float(input("Enter withdraw amount: "))
                        if amount <= balance:
                            balance -= amount
                            history.append(f"Withdrew ${amount}")
                        else:
                            print("Insufficient balance.")
                    except ValueError:
                        print("Invalid amount.")
                elif choice == '4':
                    print("Transaction History:")
                    for h in history:
                        print("-", h)
                elif choice == '5':
                    print("Thank you!")
                    break
                else:
                    print("Invalid choice.")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempts left.")
    if attempts == 0:
        print("Account locked.")

if __name__ == "__main__":
    atm_simulation()