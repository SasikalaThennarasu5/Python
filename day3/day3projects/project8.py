# 8. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ")
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    result = num1 / num2
else:
    result = "Invalid operation"
print(f"\n🧮 Result: {result}")
print("Types -> num1:", type(num1), "num2:", type(num2), "result:", type(result))