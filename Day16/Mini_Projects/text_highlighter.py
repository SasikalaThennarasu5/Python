class CapitalizedWordIterator:
    def __init__(self, text):
        # Split all words from all lines
        self.words = text.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            if word[0].isupper():
                return word
        raise StopIteration


if __name__ == "__main__":
    print("Enter multi-line text (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    full_text = "\n".join(lines)

    print("\n Capitalized Words:")
    for word in CapitalizedWordIterator(full_text):
        print(word)
