
import requests
import json
from functools import wraps

def cache_rates(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args[1]  # currency code
        if key in cache:
            print("Using cached rates.")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

class CurrencyConverter:
    def __init__(self, base_currency='USD'):
        self.base_currency = base_currency
        self.rates = {}

    @cache_rates
    def fetch_rates(self, currency):
        try:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency}")
            if response.status_code == 200:
                data = response.json()
                self.rates = data['rates']
                return self.rates
            else:
                raise Exception("API Error: Unable to fetch rates.")
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def convert(self, amount, from_currency, to_currency):
        rates = self.fetch_rates(from_currency)
        if to_currency not in rates:
            print("Invalid target currency.")
            return None
        converted = amount * rates[to_currency]
        return converted

    def list_supported_currencies(self):
        rates = self.fetch_rates(self.base_currency)
        return list(rates.keys())

    def mock_historical_rates(self):
        for i in range(3):
            yield { "day": f"Day-{i+1}", "rate": round(0.8 + 0.1 * i, 2) }

if __name__ == "__main__":
    converter = CurrencyConverter()
    while True:
        print("\n1. Convert Currency")
        print("2. List Supported Currencies")
        print("3. Show Mock Historical Rates")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            from_currency = input("From Currency (e.g., USD): ").upper()
            to_currency = input("To Currency (e.g., EUR): ").upper()
            try:
                amount = float(input("Amount: "))
                result = converter.convert(amount, from_currency, to_currency)
                if result:
                    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            print("Supported Currencies:")
            print(", ".join(converter.list_supported_currencies()))
        elif choice == '3':
            for day_rate in converter.mock_historical_rates():
                print(day_rate)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
