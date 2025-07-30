import yfinance as yf
import json
import os
from functools import lru_cache

class Portfolio:
    def __init__(self, data_file="portfolio.json"):
        self.data_file = data_file
        self.stocks = {}
        self.load_portfolio()

    def load_portfolio(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.stocks = json.load(f)
        else:
            self.stocks = {}

    def save_portfolio(self):
        with open(self.data_file, "w") as f:
            json.dump(self.stocks, f)

    def add_stock(self, symbol, shares):
        self.stocks[symbol] = self.stocks.get(symbol, 0) + shares
        self.save_portfolio()

    @lru_cache(maxsize=None)
    def get_stock_price(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            return stock.info['regularMarketPrice']
        except Exception as e:
            print(f"API error for {symbol}: {e}")
            return None

    def get_portfolio_value(self):
        total = 0
        for symbol, shares in self.stocks.items():
            price = self.get_stock_price(symbol)
            if price:
                total += price * shares
        return total

# Example usage
if __name__ == "__main__":
    pf = Portfolio()
    pf.add_stock("AAPL", 10)
    pf.add_stock("GOOGL", 5)
    print(f"Total portfolio value: ${pf.get_portfolio_value():.2f}")
