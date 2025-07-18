# main.py

from cart_utils import add_to_cart, show_cart, show_categories

# Initialize cart and categories
cart = {}
available_categories = set()

# Add items to the cart
add_to_cart(cart, 501, "Laptop", 1200, "Electronics", available_categories)
add_to_cart(cart, 502, "Headphones", 150, "Electronics", available_categories)
add_to_cart(cart, 503, "Notebook", 5, "Stationery", available_categories)

# Display cart and categories
show_cart(cart)
show_categories(available_categories)
