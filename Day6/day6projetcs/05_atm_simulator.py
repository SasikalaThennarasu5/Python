# ATM Simulator
def atm(pin_input):
    def deposit(balance, amount): return balance + amount
    def withdraw(balance, amount): return balance - amount
    def change_pin(): pass  # Placeholder
    pin = "1234"
    balance = 1000
    if pin_input == pin:
        balance = deposit(balance, 500)
        balance = withdraw(balance, 200)
        print("Final balance:", balance)
    else:
        print("Invalid PIN")

atm(input("Enter PIN: "))
