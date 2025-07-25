def lazy_evaluator(operations):
    """
    Lazily evaluates a list of (a, b, op) tuples.
    Supported operations: +, -, *, /
    Yields result only when next() is called.
    """
    for a, b, op in operations:
        if op == '+':
            yield a + b
        elif op == '-':
            yield a - b
        elif op == '*':
            yield a * b
        elif op == '/':
            yield a / b if b != 0 else 'Division by zero'
        else:
            yield 'Invalid operation'

def main():
    operations = [
        (10, 5, '+'),
        (20, 4, '-'),
        (6, 7, '*'),
        (15, 3, '/'),
        (9, 0, '/'),
        (5, 2, '^')  # Invalid operation
    ]

    lazy_calc = lazy_evaluator(operations)

    print(" Lazy Evaluation Results (one at a time):")
    try:
        while True:
            print(next(lazy_calc))
    except StopIteration:
        print(" All calculations complete.")

if __name__ == "__main__":
    main()
