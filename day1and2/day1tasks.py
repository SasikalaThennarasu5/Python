# 1. Print "Hello, Python!" to the output.
print("Hello, Python!")

# 2. Print your name and age using a single print() statement.
print("Name: Alice, Age: 25")

# 3. Use print() to display three favorite fruits, separated by commas (using sep).
print("Apple", "Mango", "Strawberry", sep=", ")

# 4. Print "Python is fun" three times, all on the same line, using the end parameter.
print("Python is fun", end=" ")
print("Python is fun", end=" ")
print("Python is fun")

# 5. Use print() and f-strings to display: My favorite number is 42.
favorite_number = 42
print(f"My favorite number is {favorite_number}.")

# 6. Print the result of 5 + 7 using print().
print(5 + 7)

# 7. Write a comment in Python explaining what the print() function does.
# The print() function displays text or variables on the screen (console output).

# 8. Combine print() with variables to display a message.
name = "Alice"
age = 25
print("My name is", name, "and I am", age, "years old.")

# 9. Use print() to show the output: Apple | Banana | Cherry (use sep).
print("Apple", "Banana", "Cherry", sep=" | ")

# 10. Print your city and country, each on a separate line, in a single print() call.
print("Chennai\nIndia")

# 11. Create a variable called name and assign your first name. Print it.
name = "Alice"
print(name)

# 12. Create a variable age and assign your age. Print it.
age = 25
print(age)

# 13. Create a float variable price, assign a value, and print it.
price = 19.99
print(price)

# 14. Define a boolean variable is_student and print its value.
is_student = True
print(is_student)

# 15. Make a list of three favorite colors and print the second color.
colors = ["Red", "Blue", "Green"]
print(colors[1])  # Indexing starts from 0

# 16. Create a tuple called coordinates with two numbers and print both values.
coordinates = (10.5, 20.75)
print(coordinates[0], coordinates[1])

# 17. Define a dictionary with keys "brand" and "year" for a car. Print both values.
car = {"brand": "Toyota", "year": 2022}
print(car["brand"])
print(car["year"])

# 18. Create a set of three unique numbers and print the set.
unique_numbers = {3, 7, 10}
print(unique_numbers)

# 19. Change the value of a variable after assigning it. Print before and after.
status = "Active"
print("Before:", status)
status = "Inactive"
print("After:", status)

# 20. Assign a string to a variable, then print its type using type().
greeting = "Hello, World!"
print(type(greeting))  # Output: <class 'str'>

# 21. Assign an integer to a variable and print it.
number = 100
print(number)

# 22. Assign a float to a variable and print it.
pi = 3.14159
print(pi)

# 23. Assign a string with your favorite quote and print it.
quote = "The only way to do great work is to love what you do."
print(quote)

# 24. Assign True to a boolean variable and print it.
is_sunny = True
print(is_sunny)

# 25. Create a list of five subjects and print the last subject.
subjects = ["Math", "Science", "History", "English", "Art"]
print(subjects[-1])  # Negative indexing for last element

# 26. Make a tuple of three city names and print the first one.
cities = ("New York", "Paris", "Tokyo")
print(cities[0])

# 27. Store information about a student (name, grade) in a dictionary and print it.
student = {"name": "John", "grade": "A"}
print(student["name"])
print(student["grade"])

# 28. Add duplicate values to a set and print the set.
numbers_set = {1, 2, 2, 3, 3, 3}
print(numbers_set)  # Set automatically removes duplicates

# 29. Store different data types in a list and print each with its type using a loop.
mixed_list = [42, 3.14, "Python", True]
for item in mixed_list:
    print(item, "is of type", type(item))

# 30. Use a variable to store a value, then use type() to print its data type.
value = "Learning Python"
print(type(value))  # Output: <class 'str'>

# 31. Ask the user for their name using input(), then greet them.
name = input("What is your name? ")
print(f"Hello, {name}!")

# 32. Ask for two numbers (as input), add them, and print the result.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", num1 + num2)

# 33. Use input() to get a user's age, then print how old they'll be next year.
age = int(input("Enter your age: "))
print(f"Next year, you will be {age + 1} years old.")

# 34. Ask the user for their favorite color and print a message using f-string.
color = input("What's your favorite color? ")
print(f"Nice! {color} is a beautiful color.")

# 35. Get the user's city and country with input(), then print a formatted message.
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"You live in {city}, {country}.")

# 36. Ask for a price and a discount, calculate the discounted price, and print it using f-string.
price = float(input("Enter the price: "))
discount = float(input("Enter the discount (%): "))
discounted_price = price - (price * discount / 100)
print(f"The discounted price is: ₹{discounted_price:.2f}")

# 37. Use input() to get three hobbies, store them in a list, and print the list.
hobby1 = input("Enter your first hobby: ")
hobby2 = input("Enter your second hobby: ")
hobby3 = input("Enter your third hobby: ")
hobbies = [hobby1, hobby2, hobby3]
print("Your hobbies are:", hobbies)

# 38. Ask the user for their name and age, then print: "Alice is 25 years old."
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print(f"{user_name} is {user_age} years old.")

# 39. Write a program that asks for two numbers, multiplies them, and prints the answer with f-string.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"The product of {a} and {b} is {a * b}")

# 40. Use input() to get a string, then print its type using type().
data = input("Enter something: ")
print("You entered:", data)
print("Its type is:", type(data))

# 41. Create a variable with a value, then print its type using type().
value = 10
print(type(value))  # <class 'int'>

# 42. Use type() to check the type of user input.
user_input = input("Enter something: ")
print("Type of input:", type(user_input))  # Always str by default

# 43. Store a number as string using input(), then convert it to int and print both types.
num_str = input("Enter a number: ")
num_int = int(num_str)
print("Before conversion:", type(num_str))  # str
print("After conversion:", type(num_int))   # int

# 44. Make a list with different data types and print each value with its type (using a loop).
mixed = [10, 3.14, "Hello", True, [1, 2]]
for item in mixed:
    print(item, "is of type", type(item))

# 45. Use type() to confirm that True is of type bool.
print(type(True))  # <class 'bool'>

# 46. Ask the user for their birth year, convert it to int, and print its type.
birth_year = int(input("Enter your birth year: "))
print("Type after conversion:", type(birth_year))  # <class 'int'>

# 47. Create a tuple and print the type of the tuple.
my_tuple = (1, "apple", 3.5)
print("Tuple:", my_tuple)
print("Type:", type(my_tuple))  # <class 'tuple'>

# 48. Make a set, then print the set and its type.
my_set = {1, 2, 3}
print("Set:", my_set)
print("Type:", type(my_set))  # <class 'set'>

# 49. Use type() to determine the data type of a value inside a dictionary.
student = {"name": "Bob", "age": 20}
print("Type of 'name':", type(student["name"]))  # <class 'str'>
print("Type of 'age':", type(student["age"]))    # <class 'int'>

# 50. Write a program that asks for a number, prints its type, then prints its type after converting to float.
num = input("Enter a number: ")
print("Before conversion:", type(num))  # <class 'str'>
converted = float(num)
print("After conversion:", type(converted))  # <class 'float'>
