# 10. Online Product Discount Calculator
# Scenario: Apply dynamic discount based on product price

try:
    # Input: Price of product
    price = float(input("Enter the price of the product (₹): "))

    # Use if-elif-else for discount logic
    # 2000 → 30%, 1000–2000 → 10%, else → no discount
    if price >= 2000:
        discount_percent = 30
    elif price >= 1000:
        discount_percent = 10
    else:
        discount_percent = 0

    # Use variables and percentage calculation
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount

    print("\n------ Discount Summary ------")
    print(f"Original Price     : ₹{price:.2f}")
    print(f"Discount Applied   : {discount_percent}%")
    print(f"Discount Amount    : ₹{discount_amount:.2f}")
    print(f"Final Price to Pay : ₹{final_price:.2f}")
    print("------------------------------")

except ValueError:
    print("\n Invalid input! Please enter a valid numeric price.")
