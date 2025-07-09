#Basic While Loop Tasks (1–10)
# Task 1
i = 1
while i <= 10:
    print(i)
    i += 1

# Task 2
i = 2
while i <= 20:
    print(i)
    i += 2

# Task 3
i = 10
while i >= 1:
    print(i)
    i -= 1

# Task 4
num = int(input("Enter a number: "))
i = 1
while i <= num:
    print(i)
    i += 1

# Task 5
i, total = 1, 0
while i <= 50:
    total += i
    i += 1
print("Sum:", total)

# Task 6
num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

# Task 7
i = 1
while i <= 30:
    if i % 3 == 0:
        print(i)
    i += 1

# Task 8
while True:
    user_input = input("Enter something (type 'stop' to exit): ")
    if user_input.lower() == "stop":
        break
    print("You entered:", user_input)

# Task 9
i = 100
while i >= 50:
    print(i)
    i -= 5

# Task 10
inputs = []
i = 0
while i < 5:
    value = input(f"Enter value {i+1}: ")
    inputs.append(value)
    i += 1
print("Inputs:", inputs)

#Infinite While Loop Tasks (11–15)

# Task 11
#while True:
    #print("Welcome!")

# Task 12
correct_password = "python123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted")
        break
    else:
        print("Try again")

# Task 13
while True:
    print("1. Greet\n2. Help\n3. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("This is a menu app.")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

# Task 14
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number detected. Exiting...")
        break

# Task 15
balance = 1000
while True:
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Select: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amt = int(input("Enter amount: "))
        balance += amt
    elif choice == "3":
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient funds")
    elif choice == "4":
        break
    else:
        print("Invalid")

#While with continue Statement (16–25)
# Task 16
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# Task 17
i, count = 0, 0
while count < 5:
    num = int(input("Enter number: "))
    if num < 0:
        continue
    print("Accepted:", num)
    count += 1

# Task 18
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

# Task 19
i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

# Task 20
i, words = 0, []
while i < 10:
    word = input("Enter word: ")
    if len(word) < 3:
        continue
    words.append(word)
    i += 1
print("Accepted words:", words)

# Task 21
text = "python programming"
i = 0
while i < len(text):
    if text[i] not in "aeiou":
        i += 1
        continue
    print(text[i])
    i += 1

# Task 22
i, count = 1, 0
while i <= 100:
    if i % 2 != 0:
        count += 1
    i += 1
print("Odd numbers count:", count)

# Task 23
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    if num % 5 != 0:
        continue
    print("Multiple of 5:", num)


# Task 24
i = 1
while i <= 30:
    if i % 2 == 0 and i % 3 == 0:
        pass 
    else:
        print(i)
    i += 1


# Task 25
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(f"{i}^3 = {i**3}")
    i += 1

#While with break Statement (26–35)

# Task 26
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

# Task 27
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    print("You entered:", num)

# Task 28
password = "secret"
while True:
    entry = input("Enter password: ")
    if entry == password:
        print("Access granted")
        break

# Task 29
i = 1
while i <= 100:
    if i % 17 == 0:
        print("Found number divisible by 17:", i)
        break
    i += 1

# Task 30
while True:
    text = input("Type something (type 'exit' to stop): ")
    if text.lower() == "exit":
        break

# Task 31
while True:
    action = input("Press 'q' to quit: ")
    if action.lower() == 'q':
        break

# Task 32
i = 0
while i < 10:
    answer = input(f"Question {i+1}: ")
    if answer == "":
        print("Empty answer. Exiting.")
        break
    i += 1

# Task 33
attempts = 0
while attempts < 3:
    login = input("Enter username: ")
    if login == "admin":
        print("Login successful")
        break
    attempts += 1

# Task 34
i = 1
while True:
    product = 5 * i
    if product > 30:
        break
    print(f"5 x {i} = {product}")
    i += 1

# Task 35
i = 1
while i <= 10:
    if i == 7:
        print("Loop Interrupted")
        break
    print(i)
    i += 1

#While with pass Statement (36–40)

# Task 36
i = 1
while i <= 5:
    if i == 3:
        pass
    print(i)
    i += 1

# Task 37
i = 0
while i < 3:
    pass  # Feature to be implemented later
    i += 1

# Task 38
i = 1
while i <= 10:
    if i % 2 == 0:
        pass
    else:
        print(i)
    i += 1

# Task 39
i = 1
while i <= 5:
    if i == 2 or i == 4:
        pass
    else:
        print(i)
    i += 1

# Task 40
i = 1
while i <= 3:
    pass  # Placeholder
    i += 1

#While with else Statement (41–45)

# Task 41
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop Finished")

# Task 42
i = 0
while i < 3:
    input("Enter number: ")
    i += 1
else:
    print("All numbers entered successfully")

# Task 43
i = 2
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 2
else:
    print("This will not print")

# Task 44
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Nice job!")

# Task 45
attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == "abc123":
        print("Logged in")
        break
    attempts += 1
else:
    print("All attempts used")

#Logical/Practical Looping Use-Cases (46–50)

# Task 46
students = []
i = 0
while i < 5:
    name = input("Enter student name: ")
    students.append(name)
    i += 1
print("Students:", students)

# Task 47
todo = []
while True:
    print("1. Add\n2. View\n3. Remove\n4. Exit")
    ch = input("Choose: ")
    if ch == "1":
        task = input("Task: ")
        todo.append(task)
    elif ch == "2":
        print(todo)
    elif ch == "3":
        task = input("Task to remove: ")
        if task in todo:
            todo.remove(task)
    elif ch == "4":
        break

# Task 48
i = 0
adult_count = 0
while i < 5:
    age = int(input("Enter age: "))
    if age >= 18:
        adult_count += 1
    i += 1
print("Number of adults:", adult_count)

# Task 49
while True:
    ans = input("What is the capital of India? ").lower()
    if ans == "new delhi":
        print("Correct!")
        break
    else:
        print("Try again.")

# Task 50
secret = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("You guessed it!")
        break
    else:
        print("Wrong guess!")


