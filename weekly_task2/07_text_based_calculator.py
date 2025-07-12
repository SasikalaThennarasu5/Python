results = []

def calculate():
    try:
        a = float(input("Enter first number: "))
        op = input("Operation (+ - * /): ")
        b = float(input("Enter second number: "))
        if op == '+': res = a + b
        elif op == '-': res = a - b
        elif op == '*': res = a * b
        elif op == '/': res = a / b if b != 0 else "Infinity"
        else: return print("Invalid operation")
        results.append(res)
        print("Result:", res)
    except:
        print("Invalid input.")

while True:
    print("\n1. Calculate\n2. Show History\n3. Exit")
    choice = input("Choose: ")
    if choice == '1': calculate()
    elif choice == '2': print("History:", results)
    elif choice == '3': break
    else: print("Invalid")
