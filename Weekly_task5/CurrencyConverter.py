# Currency Converter

import requests
import datetime
import json

class CurrencyConverter:
    def __init__(self, api_key, base_currency="USD"):
        self.api_key = api_key
        self.base_currency = base_currency
        self.favorites = []
        self.api_url = "https://v6.exchangerate-api.com/v6/{}/latest/{}".format(api_key, base_currency)
        self.rates = {}
        self.load_rates()

    def load_rates(self):
        try:
            print("Fetching real-time rates...")
            response = requests.get(self.api_url)
            data = response.json()
            if data["result"] == "success":
                self.rates = data["conversion_rates"]
            else:
                print("Error fetching rates:", data.get("error-type", "Unknown error"))
        except Exception as e:
            print("Failed to fetch rates:", e)

    def convert(self, amount, from_currency, to_currency):
        if from_currency == self.base_currency:
            rate = self.rates.get(to_currency)
        else:
            self.load_rates()
            rate = self.rates.get(to_currency) / self.rates.get(from_currency)
        return round(amount * rate, 2)

    def historical_lookup(self, from_currency, to_currency, date="2023-01-01"):
        # Simulated for demo purposes (real would use another API endpoint)
        print(f"Looking up simulated historical rate for {from_currency} to {to_currency} on {date}...")
        return round(self.convert(1, from_currency, to_currency) * 0.98, 2)

    def add_favorite(self, pair):
        if pair not in self.favorites:
            self.favorites.append(pair)

    def show_trend(self, from_currency, to_currency):
        print(f"\nTrend (simulated) for {from_currency} to {to_currency} over 5 days:")
        for i in range(5):
            day = (datetime.date.today() - datetime.timedelta(days=i)).isoformat()
            rate = self.historical_lookup(from_currency, to_currency, date=day)
            bar = '=' * int(rate)
            print(f"{day}: {bar} {rate}")

# CLI for demo
if __name__ == "__main__":
    api_key = input("Enter your ExchangeRate-API key: ").strip()
    converter = CurrencyConverter(api_key)

    while True:
        print("\n--- Currency Converter ---")
        print("1. Convert\n2. Historical Lookup\n3. Add Favorite Pair\n4. Show Favorites\n5. Show Trend\n6. Exit")
        choice = input("Choose: ")

        if choice == '1':
            amt = float(input("Amount: "))
            from_curr = input("From currency (e.g. USD): ").upper()
            to_curr = input("To currency (e.g. INR): ").upper()
            result = converter.convert(amt, from_curr, to_curr)
            print(f"{amt} {from_curr} = {result} {to_curr}")
        elif choice == '2':
            from_curr = input("From currency: ").upper()
            to_curr = input("To currency: ").upper()
            date = input("Date (YYYY-MM-DD): ")
            rate = converter.historical_lookup(from_curr, to_curr, date)
            print(f"Rate on {date}: 1 {from_curr} = {rate} {to_curr}")
        elif choice == '3':
            pair = input("Enter currency pair (e.g. USD->INR): ")
            converter.add_favorite(pair)
        elif choice == '4':
            print("Favorite Pairs:")
            for fav in converter.favorites:
                print(fav)
        elif choice == '5':
            from_curr = input("From currency: ").upper()
            to_curr = input("To currency: ").upper()
            converter.show_trend(from_curr, to_curr)
        elif choice == '6':
            print("Exiting.")
            break
