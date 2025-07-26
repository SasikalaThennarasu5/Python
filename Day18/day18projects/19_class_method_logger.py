def log_methods(cls):
    for attr in cls.__dict__:
        if callable(getattr(cls, attr)) and not attr.startswith("__"):
            original = getattr(cls, attr)
            def wrapper(self, *args, _original=original, **kwargs):
                print(f"Calling method: {_original.__name__} with args: {args}")
                return _original(self, *args, **kwargs)
            setattr(cls, attr, wrapper)
    return cls
