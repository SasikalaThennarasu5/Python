# Exception Handling and Edge Cases

# 1. Use try-except block to catch StopIteration and continue a new list
def example_1():
    print("1. Catch StopIteration and continue another list:")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    it1 = iter(list1)
    it2 = iter(list2)

    while True:
        try:
            print(next(it1), end=" ")
        except StopIteration:
            print("\nSwitching to second list:")
            break

    for i in it2:
        print(i, end=" ")
    print("\n")


# 2. Iterator that raises a custom error after 5 items
class CustomLimitIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 5:
            raise RuntimeError("Custom Error: Iterator exceeded limit of 5 items.")
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val


# 3. Modify __next__() to raise StopIteration with a custom message (display only)
class CustomStopMessageIterator:
    def __init__(self, items):
        self.items = items
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.items):
            raise StopIteration("No more items left in the list!")
        val = self.items[self.idx]
        self.idx += 1
        return val


# 4. Safe iterator wrapper that ends silently without exception
class SafeIterator:
    def __init__(self, iterable):
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            return None  # Instead of raising, return None


# 5. Iterator that prints a warning before stopping
class WarningBeforeStopIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            print("⚠️  Warning: No more items, stopping iteration.")
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val


# -----------------------------
# Run all examples
if __name__ == "__main__":
    example_1()

    print("2. Custom error after 5 items:")
    try:
        for item in CustomLimitIterator([10, 20, 30, 40, 50, 60, 70]):
            print(item, end=" ")
    except RuntimeError as e:
        print("\nException caught:", e)
    print()

    print("\n3. Custom StopIteration message:")
    it = CustomStopMessageIterator(["a", "b"])
    try:
        while True:
            print(next(it), end=" ")
    except StopIteration as e:
        print("\nIterator ended:", e)
    print()

    print("4. SafeIterator (silently ends):")
    safe_it = SafeIterator([1, 2, 3])
    while True:
        val = next(safe_it)
        if val is None:
            break
        print(val, end=" ")
    print()

    print("5. WarningBeforeStopIterator:")
    for i in WarningBeforeStopIterator(["x", "y", "z"]):
        print(i, end=" ")
    print()
