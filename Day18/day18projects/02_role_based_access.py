def access_control(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") != required_role:
                print(f"Access denied for role: {user.get('role')}")
                return None
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
