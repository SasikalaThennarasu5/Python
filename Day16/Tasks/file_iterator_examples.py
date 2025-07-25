# Iterator with Files

# Step 1: Prepare a sample file for demonstration
sample_lines = [
    "This is the first line.\n",
    "\n",  # Empty line
    "Second line is here.\n",
    "Third one.\n",
    "A fourth line with more than three words.\n"
]

with open("sample_file.txt", "w") as f:
    f.writelines(sample_lines)


# 1. Open file and use iter() + next() to read line by line
def example_1():
    print("1. Reading file line-by-line using iter() and next():")
    with open("sample_file.txt", "r") as f:
        it = iter(f)
        print(next(it).strip())
        print(next(it).strip())
        print(next(it).strip())


# 2. Handle StopIteration when file ends
def example_2():
    print("\n2. Handling StopIteration manually:")
    with open("sample_file.txt", "r") as f:
        it = iter(f)
        while True:
            try:
                line = next(it)
                print(line.strip())
            except StopIteration:
                print("End of file reached.")
                break


# 3. Custom file iterator that skips empty lines
class NonEmptyLineIterator:
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            if line.strip():
                return line.strip()
        self.file.close()
        raise StopIteration


# 4. Iterator that returns first word of each line
class FirstWordIterator:
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            words = line.strip().split()
            if words:
                return words[0]
        self.file.close()
        raise StopIteration


# 5. Iterator for lines with more than 3 words
class LinesWithMoreThanThreeWords:
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            words = line.strip().split()
            if len(words) > 3:
                return line.strip()
        self.file.close()
        raise StopIteration


# -------------------------
# Run all tasks
if __name__ == "__main__":
    example_1()
    example_2()

    print("\n3. Non-empty lines from file:")
    for line in NonEmptyLineIterator("sample_file.txt"):
        print(line)

    print("\n4. First word from each line:")
    for word in FirstWordIterator("sample_file.txt"):
        print(word)

    print("\n5. Lines with more than 3 words:")
    for line in LinesWithMoreThanThreeWords("sample_file.txt"):
        print(line)
