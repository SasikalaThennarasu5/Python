# Recursive Factorial & Fibonacci
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

print("Factorial of 5:", factorial(5))
print("Fibonacci(7):", fibonacci(7))
