import functools
from datetime import datetime

def api_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time = datetime.now().isoformat()
        try:
            result = func(*args, **kwargs)
            print(f"{time} - {func.__name__} - SUCCESS - args: {args}, kwargs: {kwargs}")
            return result
        except Exception as e:
            print(f"{time} - {func.__name__} - FAIL - args: {args}, kwargs: {kwargs} - {e}")
            raise
    return wrapper
