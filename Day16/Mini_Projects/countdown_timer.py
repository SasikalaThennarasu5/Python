
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration


if __name__ == "__main__":
    try:
        start = int(input("Enter countdown start number: "))
        print("Countdown:")
        for number in Countdown(start):
            print(number, end="...")
        print("\n Blast off!")
    except ValueError:
        print("Please enter a valid integer.")
