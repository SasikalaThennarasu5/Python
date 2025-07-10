#Basic Function Definition and Calling (1–10)
                                       
# Task 1
def greet():
    print("Welcome to Python!")

# Task 2
def add(a, b):
    return a + b

# Task 3
def is_even(num):
    return num % 2 == 0

# Task 4
def cube(n):
    return n ** 3

# Task 5
def hello(name):
    print(f"Hello, {name}")

# Task 6
def do_nothing():
    pass

# Task 7
def greater(a, b):
    if a > b:
        print(f"{a} is greater")
    elif b > a:
        print(f"{b} is greater")
    else:
        print("Both are equal")

# Task 8
def square_area(side):
    return side * side

# Task 9
def menu(option):
    if option == "view":
        print("Viewing item")
    elif option == "add":
        print("Adding item")
    elif option == "exit":
        print("Exiting menu")
    else:
        print("Invalid option")

# Task 10
for _ in range(3):
    greet()

#Functions with Parameters and Return Values (11–15)

# Task 11
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Task 12
def full_name(fname, lname):
    return f"{fname} {lname}"

# Task 13
def is_eligible_to_vote(age):
    return age >= 18

# Task 14
def calc_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

# Task 15
def average_of_three(a, b, c):
    return (a + b + c) / 3

#Global vs Local Variables (16–20)
# Task 16
x = 100
def print_global():
    print("Global x:", x)

# Task 17
def local_scope():
    y = 50
    print("Local y:", y)

# Task 18
z = 30
def both_scope():
    a = 10
    print("Global z:", z)
    print("Local a:", a)

# Task 19
count = 0
def modify_global():
    global count
    count += 1
    print("Modified count:", count)

# Task 20
val = 5
def shadow_var():
    val = 10
    print("Inside function val:", val)

#Recursion Tasks (21–25)
# Task 21
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Task 22
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Task 23
def reverse_string(s):
    return s if len(s) == 0 else reverse_string(s[1:]) + s[0]

# Task 24
def sum_list(lst):
    return 0 if not lst else lst[0] + sum_list(lst[1:])

# Task 25
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

#*args and **kwargs Tasks (26–30)
# Task 26
def add_numbers(*args):
    return sum(args)

# Task 27
def print_args(*args):
    for arg in args:
        print(arg)

# Task 28
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Task 29
def display_all(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Task 30
def filter_integers(**kwargs):
    return {k: v for k, v in kwargs.items() if isinstance(v, int)}

#Lambda Functions (31–35)
# Task 31
add_lambda = lambda a, b: a + b

# Task 32
square = lambda x: x * x

# Task 33
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

# Task 34
# Normal version: def double(x): return x * 2
double = lambda x: x * 2

# Task 35
def multiplier(n):
    return lambda x: x * n

#Built-in Functions: map(), filter(), reduce() (36–40)

from functools import reduce

# Task 36
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4]))

# Task 37
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))

# Task 38
uppercased = list(map(str.upper, ['hello', 'world']))

# Task 39
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])

# Task 40
words = list(filter(lambda w: len(w) > 5, ["apple", "banana", "grapefruit", "kiwi"]))

#First-Class Functions (41–45)

# Task 41
def greet():
    print("Hello from greet")

greeting = greet
greeting()

# Task 42
def call_func(f):
    f()

# Task 43
def outer():
    def inner():
        return "Returned from inner"
    return inner

# Task 44
def apply_func(f, value):
    return f(value)

# Task 45
def operation(a, b, func):
    return func(a, b)

#Inner Functions (46–47)

# Task 46
def outer_message():
    def inner():
        print("Hello from inner function!")
    inner()

# Task 47
def double_outer(n):
    def double(x):
        return x * 2
    return double(n)

#OOP: self and Class-based Function (48–49)

# Task 48
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}")

# Task 49
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

#Bonus: Real-World Project-Based Function (50)
# Task 50
cart = []

def add_item(name, price):
    cart.append({'name': name, 'price': price})

def get_total():
    return sum(item['price'] for item in cart)

def apply_discount(percent):
    total = get_total()
    discount = lambda p: total - (total * p / 100)
    return discount(percent)
