import math
from decimal import Decimal as D

def sqrt(a):
    return D(math.sqrt(float(a)))

def power(a, b):
    return D(a) ** D(b)
