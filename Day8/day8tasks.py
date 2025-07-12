#List Creation & Basic Operations (Tasks 1–10)
# Task 1
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
print(students)

# Task 2
mixed = [10, 3.14, "Hello", True]
for item in mixed:
    print(item)

# Task 3
nums = []
for _ in range(5):
    nums.append(int(input("Enter a number: ")))
print(nums)

# Task 4
data = []
for _ in range(3):
    data.append(input("Enter value: "))
print(data)

# Task 5
even_numbers = []
for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers[:10])

# Task 6
ints = [1, 2, 3]
strs = ["a", "b", "c"]
print(ints, strs)

# Task 7
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print(fruits[0], fruits[-1])

# Task 8
print(fruits[-2])  # Second-last item

# Task 9
print("Total elements:", len(fruits))

# Task 10
print("Data type of list:", type(fruits))

#Accessing & Indexing (Tasks 11–15)
# Task 11
for i in range(len(fruits)):
    print(fruits[i])

# Task 12
print(fruits[::2])  # Every alternate

# Task 13
cities = ["Delhi", "Paris", "Tokyo"]
print(cities[1][2])  # Third character of second city

# Task 14
reversed_fruits = fruits[::-1]
print(reversed_fruits)

# Task 15
print(fruits[4])     # Last element using positive
print(fruits[-1])    # Last using negative

#Adding Elements to Lists (Tasks 16–20)
# Task 16
new_list = []
for _ in range(5):
    new_list.append(input("Add element: "))
print(new_list)

# Task 17
sample = ["a", "b", "d", "e"]
sample.insert(2, "c")
print(sample)

# Task 18
lst = [1, 2]
lst.extend([3, 4, 5])
print(lst)

# Task 19
students = ["Ravi", "Priya"]
name = input("Enter name to add: ")
students.append(name)
print(students)

# Task 20
a = [1, 2]
b = [3, 4]
a += b
print(a)
c = [5, 6]
a.extend(c)
print(a)

#Updating List Items (Tasks 21–25)
# Task 21
names = ["john", "alex"]
names[0] = names[0].upper()
print(names)

# Task 22
prices = [199, 299, 399, 499]
prices[2] = 999
print(prices)

# Task 23
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    if nums[i] % 2 != 0:
        nums[i] *= 2
print(nums)

# Task 24
fruits = ["apple", "banana", "grape"]
fruits[1] = "kiwi"
print(fruits)

# Task 25
nested = [["john", "doe"], [1, 2, 3]]
nested[1][2] = "done"
print(nested)

#Removing Elements (Tasks 26–30)
# Task 26
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)

# Task 27
nums = [10, 20, 30, 40]
nums.pop()
print(nums)

# Task 28
nums = [10, 20, 30, 40]
nums.pop(1)
print(nums)

# Task 29
nums = [5, 6, 7, 8, 9]
del nums[3]
print(nums)

# Task 30
nums.clear()
print("Cleared list:", nums)

#Looping Through Lists (Tasks 31–35)
# Task 31
words = ["apple", "banana", "cherry"]
for word in words:
    print(word.upper())

# Task 32
nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 != 0:
        print(n)

# Task 33
for n in nums:
    print(n**2)

# Task 34
for idx, val in enumerate(nums):
    print(f"Index {idx} = {val}")

# Task 35
items = ["apple", "banana", "apple", "grape", "apple"]
count = 0
for item in items:
    if item == "apple":
        count += 1
print("Apple count:", count)

#Nested Lists (Tasks 36–40)
# Task 36
students = [["John", 85], ["Sara", 90]]
print(students)

# Task 37
print(students[1][0])

# Task 38
students[0][1] = 95
print(students)

# Task 39
for s in students:
    print(f"Name: {s[0]}, Marks: {s[1]}")

# Task 40
students.append(["Liam", 88])
print(students)

#Concatenation, Repetition, Slicing (Tasks 41–45)
# Task 41
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# Task 42
names = ["hi", "hello"]
print(names * 3)

# Task 43
nums = [10, 20, 30, 40, 50]
print(nums[:3])

# Task 44
print(nums[1:-1])

# Task 45
nums = [1, 2, 3]
words = ["one", "two", "three"]
combined = nums + words
print(combined)

#Membership & Conditional Checks (Tasks 46–50)
# Task 46
fruits = ["apple", "banana", "mango"]
item = input("Enter fruit name: ")
print(item in fruits)

# Task 47
val = input("Enter value to remove: ")
if val in fruits:
    fruits.remove(val)
print(fruits)

# Task 48
lst = [1, 2, 3, 2, 4, 2]
target = 2
count = 0
for x in lst:
    if x == target:
        count += 1
print(f"{target} appears {count} times")

# Task 49
marks = [50, 60, 70, 80]
n = int(input("Enter a mark: "))
if n in marks:
    print("Mark found.")
else:
    print("Not found.")

# Task 50
items = ["pen", "pencil", "eraser"]
inp = input("Enter item to check: ")
print("Present" if inp in items else "Not in list")












