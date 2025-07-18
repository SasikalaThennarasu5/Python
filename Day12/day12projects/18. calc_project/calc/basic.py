from decimal import Decimal as D

def add(a, b):
    return D(a) + D(b)

def subtract(a, b):
    return D(a) - D(b)

def multiply(a, b):
    return D(a) * D(b)

def divide(a, b):
    if D(b) == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return D(a) / D(b)
