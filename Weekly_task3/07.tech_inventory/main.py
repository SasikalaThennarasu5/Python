from inventory_ops.ops import add_device, display_inventory, unique_brands

# Dictionary to hold devices
inventory = {}

# Set to keep track of unique brands
brand_set = set()

# Add sample devices
add_device(inventory, brand_set, (101, "Laptop"), "Dell", "Inspiron", 70000)
add_device(inventory, brand_set, (102, "Phone"), "Apple", "iPhone 14", 90000)
add_device(inventory, brand_set, (103, "Tablet"), "Samsung", "Galaxy Tab", 50000)
add_device(inventory, brand_set, (104, "Laptop"), "Dell", "XPS 13", 120000)  # Duplicate brand, allowed

# Display inventory
display_inventory(inventory)

# Display unique brands
unique_brands(brand_set)
