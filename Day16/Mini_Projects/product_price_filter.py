
class ProductPriceFilter:
    def __init__(self, products):
        self.products_iter = iter(products.items())

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                name, price = next(self.products_iter)
                if price > 1000:
                    return (name, price)
            except StopIteration:
                raise StopIteration


if __name__ == "__main__":
    products = {
        "Laptop": 55000,
        "Mouse": 450,
        "Keyboard": 1200,
        "Monitor": 8000,
        "Pen Drive": 700,
        "Tablet": 15000
    }

    print("🛒 Products priced above ₹1000:")
    for item in ProductPriceFilter(products):
        print(f"{item[0]} - ₹{item[1]}")
