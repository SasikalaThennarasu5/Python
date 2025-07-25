import random
import math

# 1. Use iter(callable, sentinel) to read input lines until "exit"
def example_1():
    print("1. Type something (type 'exit' to stop):")
    for line in iter(input, "exit"):
        print(f"You typed: {line}")

# 2. Custom file reader using iter() and sentinel
def example_2():
    print("\n2. Reading lines from a file using iter() and sentinel")
    with open("sample.txt", "w") as f:
        f.write("Line1\nLine2\nLine3\n")
    with open("sample.txt", "r") as f:
        for line in iter(f.readline, ""):
            print(line.strip())

# 3. Loop to fetch random numbers until >90
def example_3():
    print("\n3. Random numbers until >90:")
    rand = iter(lambda: random.randint(1, 100), 101)
    for num in rand:
        print(num, end=" ")
        if num > 90:
            break
    print("\nStopped at number > 90")

# 4. Generator-less iterator to stop on input 0
def example_4():
    print("\n4. Type numbers (0 to stop):")
    for num in iter(lambda: int(input("Enter number: ")), 0):
        print(f"You entered: {num}")

# 5. Iterator that filters out non-alphabet characters
def example_5():
    print("\n5. Filter only alphabets from input:")
    data = "a1b2c3!@#dEfG"
    alpha_iter = iter(c for c in data if c.isalpha())
    for ch in alpha_iter:
        print(ch, end=" ")
    print()

# 6. Infinite number stream using lambda and iter()
def example_6():
    print("\n6. First 5 numbers from infinite stream:")
    stream = iter(lambda: random.randint(0, 9), None)  # infinite
    for i, val in enumerate(stream):
        print(val, end=" ")
        if i == 4:
            break
    print()

# 7. Calculator input stream using iter(input, 'done')
def example_7():
    print("\n7. Calculator (type 'done' to finish):")
    for expr in iter(input, "done"):
        try:
            print("Result:", eval(expr))
        except Exception as e:
            print("Error:", e)

# 8. Lazy square root generator
def example_8():
    print("\n8. Lazy square root generator:")
    nums = [1, 4, 9, 16, 25, -1]
    sqrt_iter = iter(lambda: nums.pop(0) if nums else -1, -1)
    for num in sqrt_iter:
        if num < 0:
            print("Stopping on negative number.")
            break
        print(f"√{num} = {math.sqrt(num)}")

# 9. Iterating with next() and index
def example_9():
    print("\n9. Iterating with index and next():")
    data = ["a", "b", "c"]
    it = iter(data)
    index = 0
    while True:
        try:
            item = next(it)
            print(f"{index}: {item}")
            index += 1
        except StopIteration:
            break

# 10. Use iter() with stop-signal and count iterations
def example_10():
    print("\n10. Count how many times loop runs:")
    count = 0
    def counter():
        nonlocal count
        count += 1
        return random.randint(1, 10)

    stop_value = 5
    for val in iter(counter, stop_value):
        print(f"Generated: {val}")
    print(f"Loop ran {count} times before hitting stop value {stop_value}")


# ------------------------------
# run all tasks
if __name__ == "__main__":
    # example_1()
    example_2()
    example_3()
    # example_4()
    example_5()
    example_6()
    # example_7()
    example_8()
    example_9()
    example_10()
