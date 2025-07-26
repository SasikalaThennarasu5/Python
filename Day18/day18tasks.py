# ✅ Basic Decorator Tasks
# 1. Print “Function started” before execution:

def start_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)
    return wrapper
# 2. Print the name of the function being called:

def name_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
# 3. Count how many times a function is called:

def count_decorator(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function called {count} times")
        return func(*args, **kwargs)
    return wrapper
# 4. Return the square of the function's return value:

def square_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper
# 5. Convert the return value to uppercase:

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
# 6. Log the function’s arguments and return value:

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper
# 7. Add logging before and after any function:

def before_after_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper
# 8. Add exception handling:

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception caught: {e}")
    return wrapper
# 9. Print the execution time of a function:

import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper
1# 0. Log the current datetime before a function runs:

from datetime import datetime
def datetime_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Current datetime: {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

# ✅ Decorators with *args and **kwargs
# 1. Accept any number of arguments and log them:


def log_args_kwargs(func):
    def wrapper(*args, **kwargs):
        print(f"Positional: {args}, Keyword: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
# 2. Decorator that sums all arguments passed to a function:


def sum_arguments_decorator(func):
    def wrapper(*args, **kwargs):
        total = sum(arg for arg in args if isinstance(arg, (int, float)))
        print(f"Sum of args: {total}")
        return func(*args, **kwargs)
    return wrapper
# 3. Validate argument types using isinstance():

def type_check_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Invalid type: {type(arg)}")
        return func(*args, **kwargs)
    return wrapper
# 4. Ensure a string argument is not empty:

def non_empty_string_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and not arg.strip():
                raise ValueError("Empty string argument not allowed")
        return func(*args, **kwargs)
    return wrapper
# 5. Enforce at least one keyword argument:

def require_kwargs_decorator(func):
    def wrapper(*args, **kwargs):
        if not kwargs:
            raise ValueError("At least one keyword argument is required")
        return func(*args, **kwargs)
    return wrapper
# 6. Allow only int arguments:

def only_int_args(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("All arguments must be integers")
        return func(*args, **kwargs)
    return wrapper
# 7. Reverse a list argument before passing it:

def reverse_list_decorator(func):
    def wrapper(lst, *args, **kwargs):
        if isinstance(lst, list):
            lst = lst[::-1]
        return func(lst, *args, **kwargs)
    return wrapper
# 8. Convert all string arguments to lowercase:

def lowercase_args_decorator(func):
    def wrapper(*args, **kwargs):
        new_args = [arg.lower() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {k: v.lower() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper
# 9. Round float return values to 2 decimal places:


def round_float_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            return round(result, 2)
        return result
    return wrapper
# 10. Block function if block=True is passed:

def block_if_flagged(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('block', False):
            print("Function execution blocked.")
            return None
        return func(*args, **kwargs)
    return wrapper
# ✅ Decorators with Parameters (Decorator Factory)
# 1. Repeat function output n times:

def repeat_output(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
# 2. Log to a custom file path passed as an argument:

def log_to_file(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(path, 'a') as f:
                f.write(f"Calling {func.__name__} with {args}, {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator
# 3. Limit how many times a function can be called:


def limit_calls(max_calls):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_calls:
                print("Call limit reached")
                return None
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
# 4. Check if user has a specific role:

def require_role(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError("Unauthorized role")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
# 5. Enforce a minimum argument length:


def min_arg_length(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) < n:
                raise ValueError(f"At least {n} positional arguments required")
            return func(*args, **kwargs)
        return wrapper
    return decorator
# 6. Print a custom prefix before every log:

def log_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
# 7. Delay execution of the function by n seconds:

import time
def delay_execution(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Delaying for {seconds} seconds...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator
# 8. Add a custom header and footer to printed output:

def header_footer(header, footer):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator
# 9. Warn if time taken exceeds n seconds:

import time
def warn_if_slow(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            if duration > threshold:
                print(f"Warning: Execution time {duration:.2f}s exceeds {threshold}s")
            return result
        return wrapper
    return decorator
# 10. Apply a given function to the result of the decorated function:

def apply_to_result(transform_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform_func(result)
        return wrapper
    return decorator
# ✅ Multiple Decorators and Chaining
# 1. Two decorators: one to double the result and another to square it:

def double_result(func):
    def wrapper(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return wrapper

def square_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@double_result
@square_result
def get_number():
    return 3  # (3^2) = 9 → 9*2 = 18
# 2. @authenticate and @authorize:

def authenticate(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            raise PermissionError("Authentication failed")
        return func(user, *args, **kwargs)
    return wrapper

def authorize(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("authorized"):
            raise PermissionError("Authorization failed")
        return func(user, *args, **kwargs)
    return wrapper

@authenticate
@authorize
def access_resource(user):
    print("Access granted!")
# 3. @log_input and @log_output:

def log_input(func):
    def wrapper(*args, **kwargs):
        print(f"Input: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def log_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

@log_input
@log_output
def multiply(a, b):
    return a * b
# 4. Reverse a string and then uppercase it:

def reverse_string(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)[::-1]
    return wrapper

def uppercase_string(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@reverse_string
@uppercase_string
def say_hello():
    return "hello"
# 5. Format output in <p> and <div>:

def format_p(func):
    def wrapper(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return wrapper

def format_div(func):
    def wrapper(*args, **kwargs):
        return f"<div>{func(*args, **kwargs)}</div>"
    return wrapper

@format_p
@format_div
def get_message():
    return "This is a message"
# 6. CLI app chain: logging, timing, formatting:

import time

def cli_logger(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def cli_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start:.2f}s")
        return result
    return wrapper

def cli_formatter(func):
    def wrapper(*args, **kwargs):
        return f"[RESULT]: {func(*args, **kwargs)}"
    return wrapper

@cli_logger
@cli_timer
@cli_formatter
def run_cli():
    return "Command executed"
# 7. Log result, then check if it's even:

def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

def check_even(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Even" if result % 2 == 0 else "Odd")
        return result
    return wrapper

@log_result
@check_even
def get_number():
    return 10
# 8. Validate input, then transform result:

def validate_positive(func):
    def wrapper(n):
        if n < 0:
            raise ValueError("Only positive numbers allowed")
        return func(n)
    return wrapper

def square_result(func):
    def wrapper(n):
        return func(n) ** 2
    return wrapper

@square_result
@validate_positive
def process_number(n):
    return n
# 9. Simulate pipeline processing stages:

def stage1(func):
    def wrapper(data):
        print("Stage 1 processing")
        return func(data + " → stage1")
    return wrapper

def stage2(func):
    def wrapper(data):
        print("Stage 2 processing")
        return func(data + " → stage2")
    return wrapper

def stage3(func):
    def wrapper(data):
        print("Stage 3 processing")
        return func(data + " → stage3")
    return wrapper

@stage1
@stage2
@stage3
def process(data):
    return data
# 10. Use functools.wraps to preserve metadata:

from functools import wraps

def meta_preserving_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper docstring."""
        return func(*args, **kwargs)
    return wrapper

@meta_preserving_decorator
def sample_func():
    """Original docstring."""
    return "done"

# sample_func.__name__ → 'sample_func'
# sample_func.__doc__ → 'Original docstring.'

# ✅ Class-based Decorators and Built-in Types
# 1. Class-based decorator that logs before and after execution:

class LogExecution:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before execution")
        result = self.func(*args, **kwargs)
        print("After execution")
        return result

@LogExecution
def greet(name):
    print(f"Hello, {name}")
# 2. Caching/memoization using a class:

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print("Fetching from cache")
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

@Memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
# 3. Class that tracks how many instances are created:

class CountInstances:
    count = 0

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        CountInstances.count += 1
        print(f"Creating instance #{CountInstances.count}")
        return self.cls(*args, **kwargs)

@CountInstances
class Dog:
    def __init__(self, name):
        self.name = name
# 4. Decorate a class method with @classmethod and a logger:

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Math:
    @classmethod
    @log_call
    def add(cls, a, b):
        return a + b
# 5. Combine @property with custom log decorator:

def log_property(func):
    def wrapper(*args, **kwargs):
        print(f"Accessing property: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Product:
    def __init__(self, price):
        self._price = price

    @property
    @log_property
    def price(self):
        return self._price
    
# ✅ Advanced Practical Decorators
# 1. API rate limiting (allow only 5 calls per minute):

import time

class RateLimiter:
    def __init__(self, func):
        self.func = func
        self.calls = []
        self.limit = 5  # max 5 calls
        self.period = 60  # per 60 seconds

    def __call__(self, *args, **kwargs):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < self.period]

        if len(self.calls) >= self.limit:
            raise Exception("Rate limit exceeded")
        
        self.calls.append(now)
        return self.func(*args, **kwargs)

@RateLimiter
def access_api():
    print("API accessed")
# 2. Retry failed function up to 3 times:

def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

@retry(3)
def unstable_function():
    import random
    if random.randint(0, 1):
        raise ValueError("Random failure")
    return "Success"
# 3. Track time of each call and store in a log list:

call_log = []

def track_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        call_log.append((func.__name__, duration))
        return result
    return wrapper

@track_time
def slow_function():
    time.sleep(1)
    return "Done"
# 4. Check for a valid API token before executing:


def require_token(valid_token):
    def decorator(func):
        def wrapper(token, *args, **kwargs):
            if token != valid_token:
                raise PermissionError("Invalid token")
            return func(token, *args, **kwargs)
        return wrapper
    return decorator

@require_token("my_secure_token")
def secure_action(token):
    print("Secure action executed")
# 5. Encrypt and decrypt return values using a custom key:

def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def secure_encrypt(key):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            encrypted = xor_encrypt_decrypt(result, key)
            print(f"Encrypted: {encrypted}")
            decrypted = xor_encrypt_decrypt(encrypted, key)
            print(f"Decrypted: {decrypted}")
            return decrypted
        return wrapper
    return decorator

@secure_encrypt("secret")
def get_sensitive_data():
    return "Password123"
