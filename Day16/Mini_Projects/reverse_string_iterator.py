
class ReverseStringIterator:
    def __init__(self, input_str):
        if not input_str:
            raise ValueError("Input string cannot be empty.")
        self.input_str = input_str
        self.index = len(input_str) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            char = self.input_str[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration


# --- Usage ---
if __name__ == "__main__":
    try:
        user_input = input("Enter a string: ")
        rev_iter = ReverseStringIterator(user_input)

        print("Characters in reverse:")
        for ch in rev_iter:
            print(ch)
    except ValueError as ve:
        print("Error:", ve)
