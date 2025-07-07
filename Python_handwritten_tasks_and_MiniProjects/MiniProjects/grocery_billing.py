# 3. Grocery Billing System
# Scenario: A grocery store wants to automate billing

# Predefined dictionary: item → price
grocery_prices = {
    "rice": 50,
    "wheat": 40,
    "milk": 30,
    "eggs": 6,
    "bread": 25,
    "oil": 120,
    "sugar": 45,
    "tea": 150,
    "coffee": 200,
    "fruits": 100
}

# Use list to input selected items
selected_items = input("Enter the items you want to buy (comma-separated): ").lower().split(',')

# Use for loop to calculate total bill
total = 0
print("\n--------- Bill ---------")
for item in selected_items:
    item = item.strip()
    if item in grocery_prices:
        price = grocery_prices[item]
        total += price
        print(f"{item.title():<10} : ₹{price}")
    else:
        print(f"{item.title():<10} : Not Available")

# If total > ₹1000, apply 10% discount
if total > 1000:
    discount = total * 0.10
    final_amount = total - discount
    discount_msg = f"10% Discount Applied: -₹{discount:.2f}"
else:
    final_amount = total
    discount_msg = "No Discount Applied"

# Use conditional logic + f-string for output
print("\n---------------------------")
print(f"Total Amount : ₹{total:.2f}")
print(f"{discount_msg}")
print(f"Final Amount : ₹{final_amount:.2f}")
print("---------------------------")
