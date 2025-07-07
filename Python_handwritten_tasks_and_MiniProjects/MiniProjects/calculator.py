# 13. Simple Calculator
# Scenario: A command-line calculator

try:
    # Input: Two numbers and an operation (+, -, *, /)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    # Use if-elif-else to perform the correct operation
    if operation == '+':
        result = num1 + num2
        symbol = "+"
    elif operation == '-':
        result = num1 - num2
        symbol = "-"
    elif operation == '*':
        result = num1 * num2
        symbol = "*"
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            symbol = "/"
        else:
            print("\n Error: Division by zero is not allowed.")
            exit()
    else:
        print("\n Invalid operation! Use +, -, *, or /.")
        exit()

    # Display formatted result
    print("\n------ Calculator Result ------")
    print(f"{num1} {symbol} {num2} = {result}")
    print("--------------------------------")

except ValueError:
    print("\n Invalid input! Please enter valid numbers.")
