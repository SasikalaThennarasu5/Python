
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit        # how many numbers to generate
        self.count = 0            # counter for how many generated
        self.a, self.b = 0, 1     # first two Fibonacci numbers

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

# Example usage
if __name__ == "__main__":
    print(" Fibonacci sequence using for loop:")
    for num in FibonacciIterator(10):
        print(num, end=' ')
    
    print("\n\n Fibonacci sequence using manual next():")
    fib = FibonacciIterator(5)
    while True:
        try:
            print(next(fib), end=' ')
        except StopIteration:
            break
