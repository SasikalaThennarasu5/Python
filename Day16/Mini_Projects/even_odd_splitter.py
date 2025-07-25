
class EvenIterator:
    def __init__(self, numbers):
        self.numbers = [num for num in numbers if num % 2 == 0]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value


class OddIterator:
    def __init__(self, numbers):
        self.numbers = [num for num in numbers if num % 2 != 0]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value


# --- Usage ---
if __name__ == "__main__":
    data = [10, 13, 4, 7, 8, 9, 12, 17, 20, 21]

    print("Even Numbers:")
    even_iter = EvenIterator(data)
    for num in even_iter:
        print(num, end=" ")

    print("\n\nOdd Numbers:")
    odd_iter = OddIterator(data)
    for num in odd_iter:
        print(num, end=" ")
