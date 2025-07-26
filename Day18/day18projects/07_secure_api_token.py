def validate_token(valid_token):
    def decorator(func):
        def wrapper(token, *args, **kwargs):
            if token != valid_token:
                raise PermissionError("Invalid token")
            return func(token, *args, **kwargs)
        return wrapper
    return decorator
