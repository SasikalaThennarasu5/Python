def remove_nulls(func):
    def wrapper(data):
        return func([x for x in data if x is not None])
    return wrapper

def strip_whitespace(func):
    def wrapper(data):
        return func([x.strip() for x in data])
    return wrapper

def to_lowercase(func):
    def wrapper(data):
        return func([x.lower() for x in data])
    return wrapper
