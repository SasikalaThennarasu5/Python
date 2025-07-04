#  7. Product Discount System
product = input("Enter product name: ")
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
final_price = price
final_price -= (price * discount / 100)
print(f"Product: {product}, Final Price after {discount}% discount: ₹{final_price}")