import re

# 1. PaginationIterator – navigate blog articles page-by-page
class PaginationIterator:
    def __init__(self, items, page_size=3):
        self.items = items
        self.page_size = page_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        start = self.index
        end = min(self.index + self.page_size, len(self.items))
        page = self.items[start:end]
        self.index += self.page_size
        return page


# 2. TransactionIterator – returns 5 transactions at a time
class TransactionIterator:
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.transactions):
            raise StopIteration
        chunk = self.transactions[self.index:self.index + 5]
        self.index += 5
        return chunk


# 3. SensorDataIterator – stops when threshold is breached
class SensorDataIterator:
    def __init__(self, data_stream, threshold):
        self.data = data_stream
        self.index = 0
        self.threshold = threshold

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        if val > self.threshold:
            raise StopIteration
        self.index += 1
        return val


# 4. EmailValidatorIterator – yields only valid emails
class EmailValidatorIterator:
    def __init__(self, emails):
        self.emails = emails
        self.index = 0
        self.pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.emails):
            email = self.emails[self.index]
            self.index += 1
            if self.pattern.match(email):
                return email
        raise StopIteration


# 5. ProductStockIterator – yields products below stock threshold
class ProductStockIterator:
    def __init__(self, products, threshold):
        self.products = products
        self.threshold = threshold
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            if product["stock"] < self.threshold:
                return product
        raise StopIteration


# -----------------------------------
# Run all tasks
if __name__ == "__main__":
    print("1. PaginationIterator (Blog Articles):")
    blog_articles = [f"Article {i}" for i in range(1, 11)]
    for page in PaginationIterator(blog_articles, page_size=4):
        print("Page:", page)
    print()

    print("2. TransactionIterator (5 at a time):")
    transactions = [f"TXN{i:03d}" for i in range(1, 17)]
    for chunk in TransactionIterator(transactions):
        print("Batch:", chunk)
    print()

    print("3. SensorDataIterator (threshold=70):")
    readings = [45, 50, 60, 65, 71, 68, 66]
    for value in SensorDataIterator(readings, threshold=70):
        print("Reading:", value)
    print()

    print("4. EmailValidatorIterator:")
    emails = ["user@example.com", "invalid@", "test@domain.com", "no-at.com", "good.email@site.org"]
    for valid in EmailValidatorIterator(emails):
        print("Valid email:", valid)
    print()

    print("5. ProductStockIterator (threshold=10):")
    products = [
        {"name": "Item A", "stock": 5},
        {"name": "Item B", "stock": 12},
        {"name": "Item C", "stock": 8},
        {"name": "Item D", "stock": 15},
    ]
    for product in ProductStockIterator(products, threshold=10):
        print(f"Low stock: {product['name']} - Stock: {product['stock']}")
