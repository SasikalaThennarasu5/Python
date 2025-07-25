import time
import csv

# 1. Infinite generator for multiples of 5
def infinite_multiples_of_5():
    num = 1
    while True:
        yield num * 5
        num += 1

# 2. Chunk iterable into parts of 3
def chunk_into_threes(iterable):
    for i in range(0, len(iterable), 3):
        yield iterable[i:i+3]

# 3. Yield sorted names
def sorted_names(names):
    for name in sorted(names):
        yield name

# 4. Yield reversed lines from a file
def reversed_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        yield line.strip()

# 5. Countdown generator
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# 6. Generator that logs yield points
def logging_generator():
    for i in range(3):
        print(f"Yielding value {i}")
        yield i

# 7. Generator with send() that doubles values
def double_receiver():
    value = yield  # Prime the generator
    while True:
        print("Received:", value)
        value = yield value * 2

# 8. Return in generator + StopIteration.value
def return_value_generator():
    yield 1
    yield 2
    return "Done!"

# 9. CSV line reader
def csv_line_reader(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row

# 10. Generator that tracks how many times yield is called
def yield_tracker():
    count = 0
    while True:
        count += 1
        print(f"Yield called {count} time(s)")
        yield count

# -------------------------------
# 🔍 Demonstration of each
if __name__ == "__main__":

    print("1. Multiples of 5:")
    gen1 = infinite_multiples_of_5()
    for _ in range(5):
        print(next(gen1))

    print("\n2. Chunk into threes:")
    for chunk in chunk_into_threes([1, 2, 3, 4, 5, 6, 7]):
        print(chunk)

    print("\n3. Sorted names:")
    for name in sorted_names(['Zara', 'Mike', 'Abby', 'John']):
        print(name)

    print("\n4. Reversed lines from file:")
    # Make sure to replace with a real file path
    # for line in reversed_lines("sample.txt"):
    #     print(line)

    print("\n5. Countdown from 5:")
    for val in countdown(5):
        print(val)

    print("\n6. Logging Generator:")
    for val in logging_generator():
        print(f"Got: {val}")

    print("\n7. Generator with send() and double:")
    g = double_receiver()
    next(g)             # Prime it
    print(g.send(10))   # Output: 20
    print(g.send(7))    # Output: 14

    print("\n8. Generator with return value:")
    try:
        g2 = return_value_generator()
        print(next(g2))
        print(next(g2))
        print(next(g2))  # Raises StopIteration
    except StopIteration as e:
        print("Returned:", e.value)

    print("\n9. CSV Line Reader:")
    # actual file path:
    for line in csv_line_reader("data.csv"):
        print(line)

    print("\n10. Yield Tracker:")
    y = yield_tracker()
    print(next(y))
    print(next(y))
    print(next(y))
