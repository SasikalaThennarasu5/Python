
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start  # Reset each time iter() is called
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# --- Test ---
if __name__ == "__main__":
    r = MyRange(3, 7)

    print("First iteration:")
    for i in r:
        print(i)

    print("\nSecond iteration:")
    for i in r:
        print(i)
