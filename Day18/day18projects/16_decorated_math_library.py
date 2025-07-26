import time

def validate_numeric_input(func):
    def wrapper(*args):
        if not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("All arguments must be numeric")
        return func(*args)
    return wrapper

def log_output(func):
    def wrapper(*args):
        result = func(*args)
        print(f"{func.__name__} result: {result}")
        return result
    return wrapper

def timeit(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@validate_numeric_input
@log_output
@timeit
def add(a, b): return a + b
