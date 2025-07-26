import functools

def notification(header, footer):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator
