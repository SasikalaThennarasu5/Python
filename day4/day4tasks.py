

# ✅ 🔁Basic For Loop Tasks (1–10)

# Task 1
print("Task 1:")
for item in ["Pen", "Pencil", "Eraser"]:
    print(item)

# Task 2
print("\nTask 2:")
for char in "Vetri":
    print(char)

# Task 3
print("\nTask 3:")
for i in range(1, 11):
    print(i)

# Task 4
print("\nTask 4:")
for i in range(1, 21, 2):
    print(i)

# Task 5
print("\nTask 5:")
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
for color in colors:
    print(color)

# Task 6
print("\nTask 6:")
for i in range(10, 0, -1):
    print(i)

# Task 7
print("\nTask 7:")
n = 5  # Replace with input("Enter a number: ")
for i in range(1, n + 1):
    print(i)

# Task 8
print("\nTask 8:")
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Task 9
print("\nTask 9:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Task 10
print("\nTask 10:")
total = 0
for i in range(1, 51):
    total += i
print("Sum:", total)

#✅ 🔠 For Loop with Strings (11–15)

# Task 11
print("\nTask 11:")
for ch in "Technology":
    if ch.lower() in 'aeiou':
        print(ch)

# Task 12
print("\nTask 12:")
text = "Engineering"
count = 0
for ch in text:
    if ch.lower() in 'aeiou':
        count += 1
print("Number of vowels:", count)

# Task 13
print("\nTask 13:")
text = "Python Loop Practice"
count = 0
for ch in text:
    if ch.islower():
        count += 1
print("Lowercase letters:", count)

# Task 14
print("\nTask 14:")
for word in "Learn Python Fast".split():
    print(word)

# Task 15
print("\nTask 15:")
s = "Python"
reversed_str = ""
for ch in s:
    reversed_str = ch + reversed_str
print(reversed_str)

#✅ 🔢 Range() with For Loop (16–20)

# Task 16
print("\nTask 16:")
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# Task 17
print("\nTask 17:")
for i in range(2, 21, 2):
    print(i)

# Task 18
print("\nTask 18:")
start, end = 3, 7
for i in range(start, end + 1):
    print(i)

# Task 19
print("\nTask 19:")
i = 1
while (2 ** i) <= 1024:
    print(2 ** i)
    i += 1

# Task 20
print("\nTask 20:")
for i in range(1, 11):
    print(f"{i}^2 = {i ** 2}")

#✅ 🔂 Control Statements – break, continue, pass, else (21–30)

# Task 21
print("\nTask 21:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Task 22
print("\nTask 22:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Task 23
print("\nTask 23:")
for i in range(3):
    pass

# Task 24
print("\nTask 24:")
nums = [1, 3, -2, 4, 5]
for num in nums:
    if num < 0:
        break
    print(num)

# Task 25
print("\nTask 25:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Task 26
print("\nTask 26:")
for i in range(1, 4):
    print(i)
else:
    print("Loop complete!")

# Task 27
print("\nTask 27:")
items = ["Go", "Run", "Stop", "Wait"]
for item in items:
    if item == "Stop":
        break
    print(item)

# Task 28
print("\nTask 28:")
for ch in "VetriTech":
    if ch == 'T':
        continue
    print(ch)

# Task 29
print("\nTask 29:")
for i in range(1, 11):
    if i % 3 == 0:
        pass
    print(i)

# Task 30
print("\nTask 30:")
for i in range(1, 6):
    print(i)
else:
    print("Completed without break")

#✅ 🔁 enumerate() Function (31–35)

# Task 31
print("\nTask 31:")
for i, ch in enumerate("Python"):
    print(i, ch)

# Task 32
print("\nTask 32:")
fruits = ["Apple", "Banana", "Cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Task 33
print("\nTask 33:")
for i, ch in enumerate("Hello World"):
    print(f"Position {i}: {ch}")

# Task 34
print("\nTask 34:")
students = ["John", "Priya", "Kumar"]
for roll, student in enumerate(students, start=101):
    print(f"Roll No: {roll} - {student}")

# Task 35
print("\nTask 35:")
def print_menu(menu):
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")
print_menu(["Idly", "Dosa", "Poori"])

#✅ 🔁 Nested For Loops (36–45)

# Task 36
print("\nTask 36:")
for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# Task 37
print("\nTask 37:")
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()

# Task 38
print("\nTask 38:")
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Task 39
print("\nTask 39:")
a = [1, 2]
b = ['A', 'B']
for i in a:
    for j in b:
        print(i, j)

# Task 40
print("\nTask 40:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j}", end="\t")
    print()

# Task 41
print("\nTask 41:")
ch = ord('A')
for i in range(1, 4):
    for j in range(i):
        print(chr(ch), end=" ")
    ch += 1
    print()

# Task 42
print("\nTask 42:")
name = "Ram"
for i in range(1, len(name) + 1):
    for j in range(i):
        print(name[j], end="")
    print()

# Task 43
print("\nTask 43:")
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

# Task 44
print("\nTask 44:")
for _ in range(3):
    for _ in range(3):
        print("#", end=" ")
    print()

# Task 45
print("\nTask 45:")
rows, cols = 4, 5
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()

#✅ 🧠 Logic-Based Loop Tasks (46–50)

# Task 46
print("\nTask 46:")
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# Task 47
print("\nTask 47:")
nums = [4, 12, 7, 9, 5]
maximum = nums[0]
for num in nums:
    if num > maximum:
        maximum = num
print("Max:", maximum)

# Task 48
print("\nTask 48:")
lst = [1, 2, 3, 4]
reversed_lst = []
for i in lst:
    reversed_lst = [i] + reversed_lst
print(reversed_lst)

# Task 49
print("\nTask 49:")
n = 7
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Task 50
print("\nTask 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
