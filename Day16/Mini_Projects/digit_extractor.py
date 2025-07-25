
class DigitExtractor:
    def __init__(self, mixed_string):
        self.digits = [int(ch) for ch in mixed_string if ch.isdigit()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.digits):
            raise StopIteration
        digit = self.digits[self.index]
        self.index += 1
        return digit


if __name__ == "__main__":
    test_string = input("Enter a mixed string (e.g., abc123def456): ")
    
    print("\n Extracted digits:")
    for digit in DigitExtractor(test_string):
        print(digit, end=' ')
