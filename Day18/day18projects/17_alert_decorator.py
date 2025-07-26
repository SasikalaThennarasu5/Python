def alert_if_exceeds(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f"ALERT: {result} exceeds threshold {threshold}")
            return result
        return wrapper
    return decorator
