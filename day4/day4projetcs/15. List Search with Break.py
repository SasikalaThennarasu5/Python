# Project 15: List Search with Break
print("\nProject 15: List Search with Break")
products = ["Milk", "Sugar", "Tea", "Coffee"]
search = "Tea"
for item in products:
    if item.lower() == search.lower():
        print("Product Found")
        break
else:
    print("Product Not Found")