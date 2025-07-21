def add_to_cart(cart, product_id, quantity):
    cart.append((product_id, quantity))

def remove_from_cart(cart, product_id):
    return [item for item in cart if item[0] != product_id]

def checkout(cart, products):
    total = 0
    for pid, qty in cart:
        name, price, stock = products[pid]
        total += price * qty
    return total
