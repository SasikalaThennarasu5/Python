def validate_types(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, expected_types[i]):
                    raise TypeError(f"Argument {i+1} must be {expected_types[i].__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
