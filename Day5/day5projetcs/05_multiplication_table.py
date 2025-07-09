# Project 5: Multiplication Table Generator
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
else:
    print("Table completed")
