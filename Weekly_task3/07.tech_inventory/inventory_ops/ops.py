def add_device(inventory: dict, brand_set: set, device_id: tuple, brand: str, model: str, price: int):
    if device_id in inventory:
        print(f"Device {device_id} already exists.")
        return
    inventory[device_id] = {
        "brand": brand,
        "model": model,
        "price": price
    }
    brand_set.add(brand)
    print(f"Added device {device_id}: {brand} {model} at ₹{price}")


def display_inventory(inventory: dict):
    print("\n--- Inventory ---")
    for device_id, info in inventory.items():
        print(f"ID: {device_id} | Brand: {info['brand']} | Model: {info['model']} | Price: ₹{info['price']}")


def unique_brands(brand_set: set):
    print("\nUnique Brands in Inventory:")
    for brand in sorted(brand_set):
        print(f"- {brand}")
