# 14. Product Search Tool
# Scenario: Search if a product is in stock

# Predefined list of products
products = ["rice", "milk", "bread", "eggs", "oil", "sugar", "tea", "coffee", "fruits", "vegetables"]

# Input: Product to search
search_item = input("Enter product name to search: ").strip().lower()

# Use for loop + if to find match
found = False
for item in products:
    if item == search_item:
        found = True
        break

# If found → "Available", else → "Out of stock"
print("\n------ Product Search Result ------")
if found:
    print(f" '{search_item.title()}' is Available in stock.")
else:
    print(f" '{search_item.title()}' is Out of Stock.")
print("-----------------------------------")
