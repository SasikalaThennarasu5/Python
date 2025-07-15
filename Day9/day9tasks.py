# 1. Tuple Basics
# Empty tuple
t1 = ()
print(type(t1))

# Tuple with mixed types
t2 = (10, "hello", 3.14)
for item in t2:
    print(item)

# Single element tuple
t3 = (42,)
print(type(t3))

# Convert list to tuple
lst = [1, 2, 3, 4, 5]
t4 = tuple(lst)
print(t4)

# Convert string to tuple of characters
t5 = tuple("Python")
print(t5)
#2. Tuple Indexing and Slicing

t = (10, 20, 30, 40, 50, 60, 70)

# First and last
print(t[0], t[-1])

# Middle 3 elements
print(t[2:5])

# Reverse
print(t[::-1])

# Every second element
print(t[::2])

# Negative slicing
print(t[-4:-1])
# 3. Tuple Immutability
t = (1, 2, 3)

# Attempt change
try:
    t[0] = 10
except TypeError as e:
    print("Error:", e)

# Replace a value
lst = list(t)
lst[1] = 99
t2 = tuple(lst)
print(t2)

# Add new value
t3 = t + (4,)
print(t3)

# Remove an item
lst = list(t)
lst.remove(2)
t4 = tuple(lst)
print(t4)

# del on index not allowed
try:
    del t[0]
except TypeError as e:
    print("Error:", e)
#4. Tuple Operations

t1 = (1, 2)
t2 = (3, 4)

# Concatenate
print(t1 + t2)

# Repeat
print(t1 * 3)

# Existence
print(2 in t1)

# Length
print(len(t1 + t2))

# Count element
t3 = (1, 2, 1, 3, 1)
print(t3.count(1))
# 5. Tuple Functions and Methods

t = (3, 1, 2, 3, 5)

# count()
print(t.count(3))

# index()
print(t.index(5))

# max & min
print(max(t), min(t))

# sum
print(sum(t))

# sorted (returns list)
print(sorted(t))
#6. Iteration and Looping with Tuples

t = (1, 2, 3, 4, 5)

# for loop
for i in t:
    print(i)

# enumerate
for i, val in enumerate(t):
    print(i, val)

# while loop
i = 0
while i < len(t):
    print(t[i])
    i += 1

# Print even numbers
for val in t:
    if val % 2 == 0:
        print(val)

# Count strings starting with A
names = ("Alice", "Bob", "Anna", "Alex", "Charlie")
count = sum(1 for name in names if name.startswith("A"))
print("Starts with A:", count)

# 7. Nested Tuples

nested = ((1, 2), (3, 4), (5, 6))

# Access inner element
print(nested[1][0])

# Print sub-tuples
for sub in nested:
    print(sub)

# Sum all numbers
total = sum(x + y for x, y in nested)
print(total)

# Flatten
flat = []
for sub in nested:
    for num in sub:
        flat.append(num)
print(tuple(flat))

# Access second of third sub-tuple
print(nested[2][1])
# 8. Tuple Packing and Unpacking

# Pack values
packed = (10, 20, 30)
print(packed)

# Unpack
a, b, c = packed
print(a, b, c)

# Swap variables
x, y = 5, 10
x, y = y, x
print(x, y)

# Use *
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a, b, c)

# Nested unpacking
nested = ((1, 2), (3, 4))
(a1, a2), (b1, b2) = nested
print(a1, a2, b1, b2)
# 9. Tuple Use in Functions

# Return multiple values
def calc(a, b):
    return a + b, a * b

print(calc(3, 4))

# Pass tuple as argument
def display(t):
    for item in t:
        print(item)

display((10, 20, 30))

# Average of numbers
def avg(t):
    return sum(t) / len(t)

print(avg((10, 20, 30)))

# Return min and max
def min_max(t):
    return min(t), max(t)

print(min_max((7, 1, 5, 9)))

# Merge two tuples
def merge(t1, t2):
    return t1 + t2

print(merge((1, 2), (3, 4)))

#10. Real-Life Tuple Applications

# Coordinates
location = (12.9716, 77.5946)
print("Latitude:", location[0], "Longitude:", location[1])

# Phone book
phonebook = [("Alice", "1234"), ("Bob", "5678")]
for name, number in phonebook:
    print(f"{name}: {number}")

# RGB
pixel = (255, 128, 64)
print("R:", pixel[0], "G:", pixel[1], "B:", pixel[2])

# Exam results
results = [("Ram", 88), ("Priya", 95), ("John", 72)]
topper = max(results, key=lambda x: x[1])
print("Top Scorer:", topper)

# Immutable config
config = ("localhost", 8080, True)
print(f"Host: {config[0]}, Port: {config[1]}, Debug: {config[2]}")