from .stock import update_stock

def sell_item(item, quantity):
    print(f"Selling {quantity} units of {item}...")
    return update_stock(item, -quantity)
