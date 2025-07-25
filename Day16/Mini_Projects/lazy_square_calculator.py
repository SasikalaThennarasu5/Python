
class LazySquare:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.numbers:
            raise StopIteration(" No numbers provided to square.")
        if self.index >= len(self.numbers):
            raise StopIteration
        square = self.numbers[self.index] ** 2
        self.index += 1
        return square


if __name__ == "__main__":
    try:
        raw_input = input("Enter numbers separated by space: ")
        numbers = list(map(int, raw_input.strip().split()))

        if not numbers:
            print(" Empty input. No squares to calculate.")
        else:
            print("\n Squares (lazy generation):")
            for sq in LazySquare(numbers):
                print(sq, end=' ')
    except ValueError:
        print(" Invalid input. Please enter integers only.")
