# cart_utils.py

def add_to_cart(cart, item_id, name, price, category, available_categories):
    """Add item to cart with details stored in a dictionary."""
    item_key = (item_id,)  # Tuple for immutability
    available_categories.add(category)  # Prevent duplicate categories via set
    cart[item_key] = {
        'name': name,
        'price': price,
        'category': category
    }
    print(f"Added '{name}' to the cart under category '{category}'.")


def show_cart(cart):
    """Display all items in the cart."""
    print("\nShopping Cart Contents:")
    for item_key, item in cart.items():
        print(f"Item ID: {item_key[0]}, Name: {item['name']}, Price: ${item['price']}, Category: {item['category']}")
    print("-" * 40)


def show_categories(available_categories):
    """Display unique product categories."""
    print(f"\nAvailable Categories: {available_categories}")
    print("-" * 40)
