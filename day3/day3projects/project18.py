# 18. Movie Ticket Price Calculator
age = int(input("Enter your age: "))
if age < 12:
    price = 50
elif age <= 60:
    price = 120
else:
    price = 100
print(f"Ticket Price: ₹{price}")
