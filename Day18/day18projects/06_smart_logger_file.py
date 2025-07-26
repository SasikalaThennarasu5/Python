import functools
from datetime import datetime

def smart_logger(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open("log.txt", "a") as f:
                f.write(f"{datetime.now()} - {level} - {func.__name__} returned {result}\n")
            return result
        return wrapper
    return decorator
