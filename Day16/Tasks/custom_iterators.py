# Custom Iterator Classes

# 1. Countdown iterator
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


# 2. EvenNumbers iterator up to n
class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val = self.current
        self.current += 2
        return val


# 3. CharIterator
class CharIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        self.index += 1
        return char


# 4. FibonacciIterator
class FibonacciIterator:
    def __init__(self, max_val):
        self.a, self.b = 0, 1
        self.max = max_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val


# 5. ReverseListIterator
class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        val = self.lst[self.index]
        self.index -= 1
        return val


# 6. SquareIterator for squares of numbers in range
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current ** 2
        self.current += 1
        return val


# 7. LetterPositionIterator
class LetterPositionIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        pos = self.index
        self.index += 1
        return (char, pos)


# 8. CountdownWithStop that stops early
class CountdownWithStop:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


# 9. Iterator that yields vowels from a sentence
class VowelIterator:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.vowels = "aeiouAEIOU"

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.sentence):
            char = self.sentence[self.index]
            self.index += 1
            if char in self.vowels:
                return char
        raise StopIteration


# 10. Iterator that returns digits from a mixed string
class DigitIterator:
    def __init__(self, mixed):
        self.mixed = mixed
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.mixed):
            char = self.mixed[self.index]
            self.index += 1
            if char.isdigit():
                return char
        raise StopIteration


# -------------------------------
# Test all iterators
if __name__ == "__main__":
    print("1. Countdown:")
    for i in Countdown(5):
        print(i, end=" ")
    print("\n")

    print("2. Even Numbers up to 10:")
    for i in EvenNumbers(10):
        print(i, end=" ")
    print("\n")

    print("3. CharIterator:")
    for ch in CharIterator("Hello"):
        print(ch, end=" ")
    print("\n")

    print("4. Fibonacci up to 21:")
    for num in FibonacciIterator(21):
        print(num, end=" ")
    print("\n")

    print("5. ReverseListIterator:")
    for item in ReverseListIterator([1, 2, 3, 4]):
        print(item, end=" ")
    print("\n")

    print("6. SquareIterator 1 to 5:")
    for sq in SquareIterator(1, 5):
        print(sq, end=" ")
    print("\n")

    print("7. LetterPositionIterator:")
    for lp in LetterPositionIterator("abc"):
        print(lp, end=" ")
    print("\n")

    print("8. CountdownWithStop (start=5, stop=2):")
    for c in CountdownWithStop(5, 2):
        print(c, end=" ")
    print("\n")

    print("9. Vowels in sentence:")
    for v in VowelIterator("Beautiful day outside!"):
        print(v, end=" ")
    print("\n")

    print("10. Digits from mixed string:")
    for d in DigitIterator("a1b2c3d4"):
        print(d, end=" ")
    print("\n")
