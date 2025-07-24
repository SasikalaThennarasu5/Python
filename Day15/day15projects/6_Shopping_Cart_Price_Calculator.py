class ProductExistsError(Exception): pass

def shopping_cart():
    cart = {}
    try:
        while True:
            name = input("Product: ")
            if name in cart:
                raise ProductExistsError("Duplicate product")
            price = float(input("Price: "))
            cart[name] = price
    except ValueError:
        print("Invalid price entry")
    except ProductExistsError as e:
        print(e)
    finally:
        print("Total:", sum(cart.values()))