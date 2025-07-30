import random
import string
from functools import wraps

# Decorator to exclude similar-looking characters
def exclude_similar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        similar_chars = {'l', '1', 'I', '0', 'O'}
        password = func(*args, **kwargs)
        return ''.join(c for c in password if c not in similar_chars)
    return wrapper

# Generator to yield infinite passwords
def password_generator(length=12):
    while True:
        yield generate_password(length)

@exclude_similar
def generate_password(length=12):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")
    pool = list(string.ascii_letters + string.digits + string.punctuation)
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    gen = password_generator(12)
    for _ in range(5):
        print(next(gen))
