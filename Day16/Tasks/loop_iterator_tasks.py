import time

# 1. Compare performance of for loop vs while next() for large list
def example_1():
    print("1. For loop vs while loop (next()) performance:")

    data = list(range(1_000_000))

    # For loop
    start = time.time()
    for _ in data:
        pass
    for_time = time.time() - start
    print(f"  For loop time: {for_time:.5f} seconds")

    # While + next()
    start = time.time()
    it = iter(data)
    try:
        while True:
            next(it)
    except StopIteration:
        pass
    while_time = time.time() - start
    print(f"  While loop with next() time: {while_time:.5f} seconds")

    print(f"  {'For' if for_time < while_time else 'While'} loop is faster.\n")


# 2. Iterator that skips alternate items
class SkipAlternateIterator:
    def __init__(self, iterable):
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self.it)
        try:
            next(self.it)  # skip next
        except StopIteration:
            pass
        return val


# 3. Iterator to loop over two iterables like zip()
class ZipLikeIterator:
    def __init__(self, iterable1, iterable2):
        self.it1 = iter(iterable1)
        self.it2 = iter(iterable2)

    def __iter__(self):
        return self

    def __next__(self):
        return (next(self.it1), next(self.it2))


# 4. Peekable iterator
class PeekableIterator:
    def __init__(self, iterable):
        self.it = iter(iterable)
        self.buffer = None
        self.peeked = False

    def peek(self):
        if not self.peeked:
            self.buffer = next(self.it)
            self.peeked = True
        return self.buffer

    def __iter__(self):
        return self

    def __next__(self):
        if self.peeked:
            self.peeked = False
            return self.buffer
        return next(self.it)


# 5. Circular Iterator (infinite loop over list)
class CircularIterator:
    def __init__(self, data):
        if not data:
            raise ValueError("Cannot iterate empty list.")
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return val


# --------------------------
# Run all examples
if __name__ == "__main__":
    example_1()

    print("2. Skip alternate items:")
    for item in SkipAlternateIterator([10, 20, 30, 40, 50]):
        print(item, end=" ")
    print("\n")

    print("3. Zip-like iterator:")
    for pair in ZipLikeIterator(['a', 'b', 'c'], [1, 2, 3]):
        print(pair, end=" ")
    print("\n")

    print("4. Peekable iterator:")
    peekable = PeekableIterator(["one", "two", "three"])
    print("Peek:", peekable.peek())  # should be 'one'
    print("Next:", next(peekable))   # should also be 'one'
    print("Peek:", peekable.peek())  # 'two'
    print("Next:", next(peekable))   # 'two'
    print("Next:", next(peekable))   # 'three'
    print()

    print("5. Circular iterator (first 8 values):")
    circular = CircularIterator([1, 2, 3])
    for _ in range(8):
        print(next(circular), end=" ")
    print()
