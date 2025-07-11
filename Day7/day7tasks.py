#SECTION 1: Creating and Accessing Strings (1–10)
#✅ Create a string using single quotes, double quotes, and triple quotes.

s1 = 'Hello'
s2 = "World"
s3 = '''Python'''
print(s1, s2, s3)


#✅ Create a multiline quote using triple quotes and print it.

quote = """This is a
multi-line quote
in Python."""
print(quote)


#✅ Access the first and last characters from a string using positive and negative indexing.

text = "Python"
print("First:", text[0])
print("Last:", text[-1])


#✅ Write a program to print every character in a string using a for loop.
for ch in text:
    print(ch)


#✅ Slice a string to extract only the middle 3 characters.
text = "Learning"
mid = len(text) // 2
print(text[mid-1:mid+2])


#✅ Access and print every second character from a string using slicing.
print(text[::2])


#✅ Print all vowels in a given string using indexing and conditions.
vowels = "aeiouAEIOU"
for ch in text:
    if ch in vowels:
        print(ch, end=" ")

#✅ Extract the domain from an email like "user@gmail.com" using slicing.
email = "user@gmail.com"
domain = email[email.index("@")+1:]
print("\nDomain:", domain)


#✅ Check whether the first and last characters of a string are the same.
word = "madam"
print("Same:", word[0] == word[-1])


#✅ Print the reverse of a string using slicing.
print("Reversed:", word[::-1])

#🟦 SECTION 2: Immutability and Modification (11–15)

#❌ Try to modify a single character in a string (to understand immutability).
try:
    s = "hello"
    s[0] = "H"
except TypeError as e:
    print("Error:", e)


#✅ Write code to change the first character of a string using slicing and concatenation.
s = "hello"
s = "H" + s[1:]
print(s)


#✅ Replace a character in the middle of a string by reconstructing it.
s = "world"
s = s[:2] + "X" + s[3:]
print(s)

#✅ Create a function that replaces all vowels in a string with '*'.
def replace_vowels(s):
    return ''.join(['*' if ch in "aeiouAEIOU" else ch for ch in s])

print(replace_vowels("education"))


#✅ Create a function that returns a new string by replacing all occurrences of 'a' with '@'.
def replace_a(s):
    return s.replace('a', '@')

print(replace_a("banana"))


#🟦 SECTION 3: Deleting and Updating Strings (16–20)


#✅ Create a string and delete it using del, then try to print it (catch the error).
s = "DeleteMe"
del s
try:
    print(s)
except NameError:
    print("Variable deleted.")


#✅ Concatenate two strings using + and print the result.
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)


#✅ Write a program that takes a name and appends "Welcome!" to it.

name = "Alice"
print(name + ", Welcome!")


#✅ 19. Take user input and create a new sentence by combining it with a fixed phrase.
# name = input("Enter your name: ")
# print("Nice to meet you, " + name + "!")

#✅ 20. Repeat the word "Hello" 5 times using the * operator.
print("Hello " * 5)


#🟦 SECTION 4: Common String Methods (21–35)

#✅ Use len() to count the characters in a string.
print(len("Python"))


#✅ Convert a string to lowercase using .lower().
print("PYTHON".lower())


#✅ Convert a string to uppercase using .upper().
print("python".upper())


#✅ Remove leading and trailing whitespaces using .strip().
print("   spaced   ".strip())


#✅ Split a comma-separated string into a list using .split(',').
print("That is a bad idea.".replace("bad", "good"))


#✅ Join a list of words with - using .join().
items = "apple,banana,mango"
print(items.split(","))


#✅ Count how many times "a" appears in "banana" using .count().
words = ["learn", "code", "python"]
print("-".join(words))


#✅ Use .find() to get the first index of the letter 'o' in "Google".
print("banana".count("a"))


#✅ Create a program to convert 'Python is FUN' to 'python-is-fun'.
s = 'Python is FUN'
print(s.lower().replace(' ', '-'))


#✅ 31. Write a function that counts vowels and consonants in a string.
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = sum(1 for ch in s if ch in vowels)
    c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v, c

v, c = count_vowels_consonants("Education")
print("Vowels:", v, "Consonants:", c)


#✅ Use .replace() to remove all spaces from a string.
print("remove all spaces".replace(" ", ""))

#✅ Use .split() and a for loop to print each word on a new line.
sentence = "Print each word"
for word in sentence.split():
    print(word)

#✅ Print the middle character of a string (if odd length).
s = "hello"
if len(s) % 2 != 0:
    print("Middle character:", s[len(s)//2])

#✅ Write a function that returns the first and last characters combined.
def first_last(s):
    return s[0] + s[-1]

print(first_last("Python"))


#🟦 SECTION 5: Concatenation and Repetition (36–40)
#✅ Concatenate first name and last name with a space in between.
first = "John"
last = "Doe"
print(first + " " + last)

#✅ Write a program that asks for a name and prints it 3 times using *.
name = input("Enter your name: ")
print((name + "\n") * 3)

#✅ Create a sentence by joining five different words using +.
print("Python" + " " + "is" + " " + "easy" + " " + "to" + " " + "learn.")

#✅ Use .join() to combine a list of characters into a word.
chars = ['H', 'e', 'l', 'l', 'o']
print("".join(chars))

#✅ Take user input for a name and print “Welcome <name>” using string concatenation.
name = input("Name: ")
print("Welcome " + name)


#🟦 SECTION 6: String Formatting (41–50)
#✅ Use f-string to print “My name is John and I am 30 years old.”

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

#✅ Use .format() to insert 2 numbers and print their sum.

print("Sum of {} and {} is {}".format(10, 5, 10+5))

#✅ Use % formatting to display the price of a product: "%s costs ₹%.2f"

product = "Phone"
price = 9999.99
print("%s costs ₹%.2f" % (product, price))

#✅ Create a function that takes name and marks and prints a result using all 3 formatting methods.

def format_marks(name, marks):
    print(f"{name} scored {marks} marks.")                  # f-string
    print("{} got {}".format(name, marks))                  # .format()
    print("%s secured %d marks." % (name, marks))           # %

format_marks("Alice", 88)

#✅ Format a list of products and their prices into a formatted table using f-strings.

products = [("Pen", 10), ("Notebook", 50), ("Eraser", 5)]
for p, pr in products:
    print(f"{p:<10} ₹{pr:>5}")

#✅ Ask for user input (name, age) and print using .format().

name = input("Name: ")
age = input("Age: ")
print("Name: {}, Age: {}".format(name, age))


#✅ Print temperature conversion: "Temperature is 35°C or 95°F" using f-string.

c = 35
f = (c * 9/5) + 32
print(f"Temperature is {c}°C or {f}°F")


#✅ Format a sentence where the price changes dynamically: "The discounted price is ₹999"

price = 999
print(f"The discounted price is ₹{price}")

#✅ Write a function that accepts employee details and formats them using f-string.

def format_employee(name, id, dept):
    print(f"Employee {name} (ID: {id}) works in {dept} department.")

format_employee("Ravi", 101, "HR")


#✅ Create a dynamic weather report sentence using all formatting styles.

city = "Chennai"
temp = 38
status = "Sunny"
print(f"{city} Weather: {temp}°C, {status}")                 # f-string
print("Weather in {} is {}, {}".format(city, temp, status)) # .format()
print("Today in %s: %d°C and %s" % (city, temp, status))     # %