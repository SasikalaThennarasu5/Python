# Simple Calculator

import math

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    def evaluate(self, expression):
        try:
            result = eval(expression)
            self.history.append((expression, result))
            return result
        except Exception as e:
            return f"Error: {e}"

    def store_memory(self, value):
        self.memory = value

    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0

    def get_history(self):
        return self.history

    def convert_unit(self, value, from_unit, to_unit):
        conversions = {
            ('m', 'cm'): value * 100,
            ('cm', 'm'): value / 100,
            ('kg', 'g'): value * 1000,
            ('g', 'kg'): value / 1000,
            ('km', 'm'): value * 1000,
            ('m', 'km'): value / 1000
        }
        return conversions.get((from_unit, to_unit), "Conversion not supported")

# CLI for demo
if __name__ == "__main__":
    calc = Calculator()

    while True:
        print("\n--- Simple Calculator ---")
        print("1. Evaluate\n2. Memory Store\n3. Memory Recall\n4. History\n5. Unit Conversion\n6. Exit")
        choice = input("Choose: ")

        if choice == '1':
            expr = input("Enter expression: ")
            result = calc.evaluate(expr)
            print("Result:", result)
        elif choice == '2':
            val = float(input("Enter value to store in memory: "))
            calc.store_memory(val)
        elif choice == '3':
            print("Memory:", calc.recall_memory())
        elif choice == '4':
            for expr, res in calc.get_history():
                print(f"{expr} = {res}")
        elif choice == '5':
            val = float(input("Enter value: "))
            from_u = input("From unit (e.g. m, cm, kg, g): ")
            to_u = input("To unit: ")
            result = calc.convert_unit(val, from_u, to_u)
            print("Converted:", result)
        elif choice == '6':
            print("Exiting.")
            break
