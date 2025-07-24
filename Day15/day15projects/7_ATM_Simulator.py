class InsufficientFundsError(Exception): pass

def atm():
    balance = 1000
    try:
        choice = input("Withdraw/Deposit: ").lower()
        amount = float(input("Amount: "))
        assert amount > 0
        if choice == 'withdraw':
            if amount > balance:
                raise InsufficientFundsError("Not enough balance")
            balance -= amount
        elif choice == 'deposit':
            balance += amount
        print("Balance:", balance)
    except Exception as e:
        print(e)