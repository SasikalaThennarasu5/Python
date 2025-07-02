# 16. Odd/Even Number Identifier
num_input = input("Enter a number: ")
print("Type before conversion:", type(num_input))
num = int(num_input)
print("Type after conversion:", type(num))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")