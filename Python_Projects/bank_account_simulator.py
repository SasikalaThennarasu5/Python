
import json
from functools import wraps
from datetime import datetime

def audit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[AUDIT] {func.__name__} called at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    @audit
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount
        self.transactions.append(('deposit', amount))
        self.apply_interest()

    @audit
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.transactions.append(('withdraw', amount))

    @audit
    def transfer(self, amount, other_account):
        self.withdraw(amount)
        other_account.deposit(amount)
        self.transactions.append(('transfer', amount))

    def apply_interest(self):
        if self.balance > 1000:
            interest = self.balance * 0.01
            self.balance += interest
            self.transactions.append(('interest', interest))

    def show_transactions(self):
        for t in self.transaction_generator():
            print(t)

    def transaction_generator(self):
        for transaction in self.transactions:
            yield transaction

    def save_to_file(self, filename='account_data.json'):
        with open(filename, 'w') as f:
            json.dump({
                'name': self.name,
                'balance': self.balance,
                'transactions': self.transactions
            }, f)

# Example Usage:
if __name__ == "__main__":
    acc1 = BankAccount("Alice", 1200)
    acc2 = BankAccount("Bob", 500)

    acc1.deposit(200)
    acc1.withdraw(300)
    acc1.transfer(100, acc2)

    print("Alice's Transactions:")
    acc1.show_transactions()

    print("Bob's Transactions:")
    acc2.show_transactions()

    acc1.save_to_file("alice_account.json")
    acc2.save_to_file("bob_account.json")
