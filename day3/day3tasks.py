# Task 1: Basic Arithmetic Operations
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Task 2: Floor Division and Modulus with f-string
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Floor Division: {x} // {y} = {x // y}")
print(f"Modulus: {x} % {y} = {x % y}")

# Task 3: Exponentiation
base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

power = base ** exponent
print(f"{base} to the power of {exponent} is {power}")

# Task 4: Full Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor Division: {num1 // num2}")
print(f"Modulus: {num1 % num2}")
print(f"Exponentiation: {num1 ** num2}")

#  Task 5: Shopping App – Add Prices
item1 = float(input("Enter price of item 1: ₹"))
item2 = float(input("Enter price of item 2: ₹"))
item3 = float(input("Enter price of item 3: ₹"))

total = item1 + item2 + item3
print(f"Total price: ₹{total}")

# Task 6: Average Marks of 5 Subjects
s1 = float(input("Enter marks for subject 1: "))
s2 = float(input("Enter marks for subject 2: "))
s3 = float(input("Enter marks for subject 3: "))
s4 = float(input("Enter marks for subject 4: "))
s5 = float(input("Enter marks for subject 5: "))

average = (s1 + s2 + s3 + s4 + s5) / 5
print(f"Average Marks: {average}")

# Task 7: Celsius to Fahrenheit Conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Task 8: f-string with Arithmetic Operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# ✅ Task 9: Compare two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# ✅ Task 10: Age check
age = int(input("Enter your age: "))
print("Adult" if age > 18 else "Not Adult")

# ✅ Task 11: String comparison
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(str1 == str2, str1 != str2)

# ✅ Task 12: Higher exam score
s1 = float(input("Enter score 1: "))
s2 = float(input("Enter score 2: "))
print("Score 1 is higher" if s1 > s2 else "Score 2 is higher")

# ✅ Task 13: Range check
n = int(input("Enter a number: "))
print(10 <= n <= 100)

# ✅ Task 14: Passing mark
score = int(input("Enter score: "))
print("Pass" if score > 50 else "Fail")

# ✅ Task 15: and operator with ID
age = int(input("Enter age: "))
has_id = input("Do you have ID (yes/no): ") == "yes"
print(age > 18 and has_id)

# ✅ Task 16: or confirmation
response = input("Confirm (yes/y): ").lower()
print(response == "yes" or response == "y")

# ✅ Task 17: not operator
value = int(input("Enter a value: "))
print(not value > 10)

# ✅ Task 18: Club entry
age = int(input("Enter age: "))
dress = input("Enter dress code: ").lower()
print("Allowed" if age >= 21 and dress == "formal" else "Not Allowed")

# ✅ Task 19: Logical evaluation
b1 = input("Enter first boolean (true/false): ").lower() == "true"
b2 = input("Enter second boolean (true/false): ").lower() == "true"
print(f"AND: {b1 and b2}, OR: {b1 or b2}, NOT b1: {not b1}")

# ✅ Task 20: Pass/fail logic
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance %: "))
print("Pass" if marks >= 40 and attendance >= 75 else "Fail")

# ✅ Task 21: Assignment operators
x = 10
x += 5
x -= 2
x *= 3
x /= 2
x //= 2
x %= 4
print(x)

# ✅ Task 22: Increment by 5
n = int(input("Enter number: "))
n += 5
print(n)

# ✅ Task 23: Double square area
side = int(input("Enter side of square: "))
area = side ** 2
area *= 2
print(area)

# ✅ Task 24: Tax deduction
salary = float(input("Enter salary: "))
tax = float(input("Enter tax amount: "))
salary -= tax
print(salary)

# ✅ Task 25: Modify variable with assignment ops
v = 100
v += 10
v -= 5
v *= 2
v /= 3
v //= 2
v %= 7
print(v)

# ✅ Task 26: Bank simulator
balance = 1000
deposit = float(input("Enter deposit amount: "))
balance += deposit
withdraw = float(input("Enter withdrawal amount: "))
balance -= withdraw
print(f"Final Balance: ₹{balance}")

# ✅ Task 27: is with identical lists
l1 = [1, 2]
l2 = l1
print(l1 is l2)

# ✅ Task 28: is not with equal lists
a = [1, 2]
b = [1, 2]
print(a is not b)

# ✅ Task 29: is with immutable objects
x = 100
y = 100
print(x is y)

# ✅ Task 30: Compare 3 list references
a = [1, 2]
b = a
c = [1, 2]
print(a is b, a is not c)

# ✅ Task 31: in operator with string
letter = input("Enter letter: ")
print("a" in letter)

# ✅ Task 32: Fruit check
fruits = ["apple", "banana", "mango"]
choice = input("Enter fruit name: ").lower()
print(choice in fruits)

# ✅ Task 33: not in list
nums = [1, 2, 3, 4]
n = int(input("Enter number: "))
print(n not in nums)

# ✅ Task 34: Search in sentence
sentence = "Python is fun and powerful."
word = input("Enter word: ")
print(word in sentence)

# ✅ Task 35: Dictionary key check
d = {"name": "Alice", "age": 25}
key = input("Enter key to check: ")
print(key in d)

# ✅ Task 36: Bitwise AND, OR, XOR
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a & b, a | b, a ^ b)

# ✅ Task 37: Bitwise NOT
n = int(input("Enter number: "))
print(~n)

# ✅ Task 38: Shift operators
n = int(input("Enter number: "))
print(f"Left shift: {n << 1}, Right shift: {n >> 1}")

# ✅ Task 39: bin() and bitwise ops
x = 5
y = 3
print(f"{x} = {bin(x)}, {y} = {bin(y)}")
print(f"x & y = {x & y}, x | y = {x | y}")

# ✅ Task 40: Bit mask toggle
num = 0b1010
mask = 0b0101
toggled = num ^ mask
print(bin(toggled))

# ✅ Task 41: Vote eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")

# ✅ Task 42: Minor or adult
age = int(input("Enter age: "))
print("Minor" if age < 18 else "Adult")

# ✅ Task 43: Grade using marks
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Fail")

# ✅ Task 44: Temperature classification
temp = float(input("Enter temperature: "))
if temp > 35:
    print("Hot")
elif 25 <= temp <= 35:
    print("Warm")
else:
    print("Cool")

# ✅ Task 45: Even or Odd
n = int(input("Enter number: "))
print("Even" if n % 2 == 0 else "Odd")

# ✅ Task 46: Login check
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

# ✅ Task 47: Raining and umbrella check
rain = input("Is it raining (yes/no)? ")
if rain == "yes":
    umbrella = input("Do you have umbrella (yes/no)? ")
    if umbrella == "yes":
        print("You can go outside")
    else:
        print("Stay inside")
else:
    print("Enjoy your day!")

# ✅ Task 48: Voting with nationality
age = int(input("Enter age: "))
nation = input("Enter nationality: ")
if age >= 18 and nation.lower() == "indian":
    print("Eligible to vote")
else:
    print("Not eligible")

# ✅ Task 49: Calculator with choices
choice = input("Enter operation (add/sub): ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if choice == "add":
    print(a + b)
elif choice == "sub":
    print(a - b)
else:
    print("Invalid operation")

# ✅ Task 50: Exam result
marks = int(input("Enter marks: "))
att = int(input("Enter attendance %: "))
if marks >= 40 and att >= 75:
    print("Passed")
else:
    print("Failed")
