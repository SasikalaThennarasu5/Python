#Dictionary Basics
# 1
employees = {"Alice": 1001, "Bob": 1002, "Charlie": 1003, "David": 1004, "Eva": 1005}

# 2
contact = {"name": "Ravi", "phone": "9876543210"}
print(contact["phone"])

# 3
result = contact.get("email", "Not found")
print(result)

# 4
student_marks = {"Arun": 85}
student_marks["Divya"] = 92
print(student_marks)

# 5
student_marks["Arun"] = 90
print(student_marks)

# 6
del student_marks["Divya"]
print(student_marks)

# 7
removed_score = student_marks.pop("Arun")
print(removed_score)

# 8
info = {"a": 1, "b": 2}
print(info.popitem())  # removes and returns last inserted key-value pair

# 9
info.clear()
print(info)

# 10
print("Alice" in employees)

#Dictionary Iteration
# 11
for key in employees:
    print(key)

# 12
for value in employees.values():
    print(value)

# 13
for key, value in employees.items():
    print(key, value)

# 14
marks = {"A": 91, "B": 88, "C": 94, "D": 70}
count = sum(1 for v in marks.values() if v > 90)
print(count)

# 15
def get_keys_by_value(d, target):
    return [k for k, v in d.items() if v == target]

print(get_keys_by_value(marks, 94))

#Dictionary Methods

# 16
d1 = {"x": 1}
d2 = {"y": 2}
d1.update(d2)
print(d1)

# 17
d1.setdefault("z", 3)
print(d1)

# 18
d3 = d1.copy()
d3["x"] = 100
print(d1, d3)

# 19
t = [("a", 1), ("b", 2)]
d4 = dict(t)
print(d4)

# 20
print(list(d4.keys()))
print(list(d4.values()))

#Practical Use Cases
# 21
cart = {"apple": 3, "banana": 5}
print(cart)

# 22
grades = {"Ajay": "A", "Sneha": "B", "Kiran": "C"}
print(grades)

# 23
phonebook = {"Ravi": "9876543210"}
print(phonebook.get("Ravi", "Not found"))

# 24
inventory = {101: {"name": "Mouse", "stock": 40}, 102: {"name": "Keyboard", "stock": 20}}
print(inventory[101]["name"])

# 25
attendance = {"2025-07-16": ["Ravi", "Meena"], "2025-07-17": ["Ravi"]}
print(attendance)
 
#Nested Dictionaries
# 26
employees = {
    1: {"name": "Amit", "salary": 50000},
    2: {"name": "Bhavya", "salary": 60000}
}

# 27
print(employees[1]["salary"])

# 28
employees[3] = {"name": "Chirag", "salary": 55000}

# 29
employees[2]["salary"] = 65000

# 30
for emp in employees.values():
    print(emp["name"], emp["salary"])

#Dictionary Comprehension
# 31
squares = {n: n**2 for n in range(1, 6)}
print(squares)

# 32
nums = [1, 2, 3, 4, 5]
parity = {n: "even" if n % 2 == 0 else "odd" for n in nums}
print(parity)

# 33
words = ["apple", "banana", "kiwi"]
length_dict = {word: len(word) for word in words}
print(length_dict)

# 34
original = {"a": 1, "b": 2}
swapped = {v: k for k, v in original.items()}
print(swapped)

# 35
filtered = {k: v for k, v in marks.items() if v > 90}
print(filtered)

#Data Processing

# 36
string = "hello world"
freq = {}
for char in string:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1
print(freq)

# 37
para = "this is a test this is only a test"
words = para.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# 38
fruit_prices = {"apple": 50, "banana": 30, "mango": 80}
expensive = max(fruit_prices, key=fruit_prices.get)
print(expensive)

# 39
prices = {"apple": 50, "banana": 20}
quantities = {"apple": 3, "banana": 5}
total = sum(prices[i] * quantities[i] for i in prices)
print(total)

# 40
students = [("A", "Grade 1"), ("B", "Grade 2"), ("C", "Grade 1")]
grouped = {}
for name, grade in students:
    grouped.setdefault(grade, []).append(name)
print(grouped)

#Advanced Applications
# 41
cache = {}
def square(n):
    if n not in cache:
        cache[n] = n * n
    return cache[n]

# 42
urls = {}
def shorten(url):
    code = "url" + str(len(urls) + 1)
    urls[code] = url
    return code

# 43
translator = {"hello": "வணக்கம்", "world": "உலகம்"}
print(translator.get("hello"))

# 44
logins = {"admin": "1234"}
def login(username, password):
    return logins.get(username) == password

# 45
movies = {
    "Inception": {"year": 2010, "genre": "Sci-Fi"},
    "Up": {"year": 2009, "genre": "Animation"}
}

#Utility Tools
# 46
calc = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Divide by zero"
}
print(calc["+"](5, 3))

# 47
travel_expense = {"Chennai": 1500, "Bangalore": 2000}
print(travel_expense)

# 48
files = ["file.txt", "image.png", "doc.pdf", "note.txt"]
ext_count = {}
for file in files:
    ext = file.split(".")[-1]
    ext_count[ext] = ext_count.get(ext, 0) + 1
print(ext_count)

# 49
capitals = {"India": "New Delhi", "USA": "Washington"}
print(capitals.get("India"))

# 50
quiz = {
    "Capital of India?": "New Delhi",
    "2 + 2?": "4"
}
for q, a in quiz.items():
    ans = input(q + " ")
    print("Correct" if ans == a else "Wrong")
