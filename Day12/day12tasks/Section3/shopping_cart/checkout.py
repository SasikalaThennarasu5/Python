from .cart import cart_items

def calculate_total():
    return sum(item['price'] for item in cart_items)
