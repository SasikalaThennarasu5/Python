# Basic Exception Handling (1–10)
# Task 1: Divide two numbers, handle ZeroDivisionError and ValueError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter integers.")

# Task 2: Take user input for age, raise error if non-numeric or negative
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)

# Task 3: Open a file, handle FileNotFoundError
try:
    with open("missing_file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")

# Task 4: Read from a closed file, handle ValueError
f = open("temp.txt", "w")
f.close()
try:
    f.read()
except ValueError as e:
    print("Error:", e)

# Task 5: Handle IndexError from list
data = [10, 20, 30]
try:
    idx = int(input("Enter index: "))
    print(data[idx])
except IndexError:
    print("Index out of range.")
except ValueError:
    print("Invalid input.")

# Task 6: Handle KeyError from dictionary
user = {"name": "Alice"}
try:
    print(user["age"])
except KeyError:
    print("Key not found.")

# Task 7: Ask user to enter number, catch ValueError
try:
    num = int(input("Enter number: "))
    print("Square:", num ** 2)
except ValueError:
    print("That's not a valid number.")

# Task 8: Catch TypeError (string + int)
try:
    result = "Age: " + 25
except TypeError as e:
    print("Type Error:", e)

# Task 9: Catch AttributeError
try:
    s = "hello"
    s.append("world")
except AttributeError as e:
    print("Attribute Error:", e)

# Task 10: Handle NameError
try:
    print(x)
except NameError as e:
    print("Name Error:", e)

#Multiple Except, Else, Finally (11–20)
# Task 11: Try with else
try:
    a = int(input("A: "))
    b = int(input("B: "))
    result = a / b
except ZeroDivisionError:
    print("Zero Division")
else:
    print("Result:", result)

# Task 12: Try with finally
try:
    a = int(input("Enter a number: "))
except ValueError:
    print("Invalid")
finally:
    print("Done")

# Task 13: Multiple except blocks

try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Cannot divide")

# Task 14: Finally runs even if uncaught

try:
    raise RuntimeError("Oops")
finally:
    print("Finally ran")

# Task 15: Else + Finally

try:
    a = int(input())
    print("Square:", a ** 2)
except ValueError:
    print("Error")
else:
    print("Successful")
finally:
    print("Completed")

# Task 16: File reading with finally
try:
    f = open("sample.txt")
    print(f.read())
except Exception as e:
    print("Error:", e)
finally:
    f.close()
    print("File closed.")

# Task 17: Nested try
try:
    a = int(input("Outer: "))
    try:
        print(10 / a)
    except ZeroDivisionError:
        print("Inner: Division error")
except ValueError:
    print("Outer: Value error")

# Task 18: Multiple types in one except
try:
    val = int(input())
    print(100 / val)
except (ValueError, ZeroDivisionError) as e:
    print("Handled:", e)

# Task 19: Generic fallback
try:
    print(x / 0)
except Exception as e:
    print("Generic Error:", e)

# Task 20: Incorrect vs Correct nesting
# ❌ Incorrect
# try:
#     ...
# except:
# finally:  # Error

# ✅ Correct
try:
    a = 5
except:
    pass
finally:
    print("Correct nesting")

 # Raise Statement (21–30)
 # Task 21: Raise ValueError for negative input
num = int(input("Enter number: "))
if num < 0:
    raise ValueError("Negative not allowed")

# Task 22: Raise TypeError if argument not string
def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be string")
    print("Hello", name)
# greet(123)

# Task 23: Accept only positive int
def set_age(age):
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Positive integer only")
# set_age(-3)

# Task 24: Simulated login
def login(password):
    if password != "admin123":
        raise Exception("Incorrect password")
# login("test")

# Task 25: Raise for missing key
data = {"user": "admin"}
if "email" not in data:
    raise KeyError("Email is required")

# Task 26: Raise ZeroDivisionError manually
if True:
    raise ZeroDivisionError("Manual raise")

# Task 27: Assert even number
x = int(input("Enter even number: "))
assert x % 2 == 0, "Not even"

# Task 28: Validate email format
email = input("Enter email: ")
if "@" not in email or "." not in email:
    raise ValueError("Invalid email")

# Task 29: Check list before process
lst = []
if not lst:
    raise Exception("List is empty")

# Task 30: Check file content before read
with open("checkfile.txt", "r") as f:
    content = f.read()
    if not content:
        raise Exception("File is empty")
 
 # Custom Exceptions (31–40)
 # Task 31: NegativeNumberError
class NegativeNumberError(Exception): pass
n = -5
if n < 0:
    raise NegativeNumberError("Negative not allowed")

# Task 32: InvalidAgeError
class InvalidAgeError(Exception): pass
age = -1
if age < 0:
    raise InvalidAgeError("Invalid age")

# Task 33: InsufficientFundsError
class InsufficientFundsError(Exception): pass
balance = 100
withdraw = 200
if withdraw > balance:
    raise InsufficientFundsError("Not enough funds")

# Task 34: GradeOutOfRangeError
class GradeOutOfRangeError(Exception): pass
grade = 105
if grade > 100:
    raise GradeOutOfRangeError("Invalid grade")

# Task 35: UnauthorizedAccessError
class UnauthorizedAccessError(Exception): pass
role = "guest"
if role != "admin":
    raise UnauthorizedAccessError("Access denied")

# Task 36: InvalidFileFormatError
class InvalidFileFormatError(Exception): pass
filename = "file.exe"
if not filename.endswith(".txt"):
    raise InvalidFileFormatError("Only .txt allowed")

# Task 37: LoginAttemptsExceeded
class LoginAttemptsExceeded(Exception): pass
attempts = 4
if attempts > 3:
    raise LoginAttemptsExceeded("Too many attempts")

# Task 38: ObjectStateError
class ObjectStateError(Exception): pass
class Door:
    def __init__(self):
        self.locked = True
    def open(self):
        if self.locked:
            raise ObjectStateError("Cannot open locked door")
# Door().open()

# Task 39: FileTooLargeError
class FileTooLargeError(Exception): pass
size = 15  # in MB
if size > 10:
    raise FileTooLargeError("File too big")

# Task 40: AbsoluteZeroError
class AbsoluteZeroError(Exception): pass
temp = -300
if temp < -273.15:
    raise AbsoluteZeroError("Below absolute zero")
 
 #Exception Handling in Loops/Functions (41–45)
 # Task 41: Enter 5 valid integers
nums = []
while len(nums) < 5:
    try:
        val = int(input("Enter int: "))
        nums.append(val)
    except ValueError:
        print("Invalid")

# Task 42: Function reads file with error handle
def read_file(name):
    try:
        with open(name) as f:
            return f.read()
    except Exception as e:
        return str(e)

# Task 43: Exception in recursive factorial
def fact(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    return 1 if n == 0 else n * fact(n-1)

# Task 44: Loop with input skip
for _ in range(3):
    try:
        x = int(input("Enter int: "))
        print("Valid:", x)
    except:
        print("Skipped")

# Task 45: Try-except inside list comp
data = ["10", "abc", "20"]
ints = [int(i) for i in data if i.isdigit()]
print(ints)

# Real-Life Use Case Tasks (46–50)

# Task 46: Simple calculator
try:
    a = int(input("A: "))
    op = input("Op (+,-,*,/): ")
    b = int(input("B: "))
    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/': print(a / b)
    else: raise ValueError("Invalid op")
except Exception as e:
    print("Error:", e)

# Task 47: File copy tool
try:
    src = input("Source: ")
    dest = input("Dest: ")
    with open(src, "r") as f1, open(dest, "w") as f2:
        f2.write(f1.read())
except Exception as e:
    print("Copy failed:", e)

# Task 48: Registration form
def register(name, age, email):
    if not name or not email:
        raise ValueError("Missing info")
    if not age.isdigit() or int(age) <= 0:
        raise ValueError("Invalid age")
    print("Registered")
# register("John", "25", "john@mail.com")

# Task 49: Log exceptions to file
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR)
try:
    print(1 / 0)
except Exception as e:
    logging.error("Error occurred", exc_info=True)

# Task 50: Payment simulation
try:
    amount = float(input("Enter amount: "))
    if amount <= 0:
        raise ValueError("Invalid amount")
    print("Processing ₹", amount)
except Exception as e:
    print("Payment Error:", e)
