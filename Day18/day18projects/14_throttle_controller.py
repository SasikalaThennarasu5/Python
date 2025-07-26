import time

def throttle(limit):
    calls = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            current = time.time()
            calls[:] = [t for t in calls if current - t < 60]
            if len(calls) >= limit:
                raise Exception("Too many calls")
            calls.append(current)
            return func(*args, **kwargs)
        return wrapper
    return decorator
