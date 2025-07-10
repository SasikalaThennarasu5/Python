# Python Calculator
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y

def calculator(func, a, b):
    return func(a, b)

print("Add:", calculator(add, 5, 3))
print("Multiply:", calculator(mul, 4, 2))
