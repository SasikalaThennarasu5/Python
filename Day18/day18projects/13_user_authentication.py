def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            raise PermissionError("User not logged in")
        return func(user, *args, **kwargs)
    return wrapper
