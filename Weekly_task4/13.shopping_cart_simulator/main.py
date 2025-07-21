from cart_ops import add_to_cart, remove_from_cart, checkout

products = {
    'P001': ('Pen', 10, 100),
    'P002': ('Notebook', 50, 200),
}

cart = []
add_to_cart(cart, 'P001', 2)
add_to_cart(cart, 'P002', 1)

print("Cart Total:", checkout(cart, products))
