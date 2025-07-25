class CartIterator:
    def __init__(self, cart_items):
        if not cart_items:
            raise ValueError("⚠️ Cart is empty. Cannot fetch items.")
        self.cart = cart_items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cart):
            raise StopIteration
        item = self.cart[self.index]
        self.index += 1
        return item


if __name__ == "__main__":
    try:
        # Simulated cart input
        cart = input("Enter cart items (comma separated): ").strip().split(',')
        cart = [item.strip() for item in cart if item.strip()]

        iterator = CartIterator(cart)
        print("\n Items in your cart:")
        for item in iterator:
            print(f" {item}")

    except ValueError as ve:
        print(ve)
