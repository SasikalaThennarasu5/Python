#  2. Electricity Bill Calculator
name = input("Enter your name: ")
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 2
elif units <= 300:
    bill = units * 3
else:
    bill = units * 5
print(f"{name}, your total electricity bill is ₹{bill}")