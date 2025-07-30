import math
from functools import wraps

def radians_to_degrees(func):
    @wraps(func)
    def wrapper(x):
        return func(math.radians(x))
    return wrapper

@radians_to_degrees
def sin(x):
    return math.sin(x)

@radians_to_degrees
def cos(x):
    return math.cos(x)

@radians_to_degrees
def tan(x):
    return math.tan(x)

def log(x, base=10):
    return math.log(x, base)

def sqrt(x):
    return math.sqrt(x)

def calculator():
    print("Welcome to the Scientific Calculator! Type 'exit' to quit.")
    while True:
        expr = input("Enter expression (e.g., sin(30), log(100), 2+3): ")
        if expr.lower() == 'exit':
            break
        try:
            result = eval(expr, globals())
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"Invalid expression: {e}")

if __name__ == "__main__":
    calculator()
