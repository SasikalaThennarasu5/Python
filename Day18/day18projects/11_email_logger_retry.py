import time

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Logging call to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def retry(attempts=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retry {i+1} failed: {e}")
            print("All retries failed.")
        return wrapper
    return decorator
