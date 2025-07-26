def call_counter(func):
    func.call_count = 0
    def wrapper(*args, **kwargs):
        func.call_count += 1
        print(f"{func.__name__} called {func.call_count} times")
        return func(*args, **kwargs)
    return wrapper
