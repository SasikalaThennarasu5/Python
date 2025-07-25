
class WordSplitter:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        else:
            raise StopIteration


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Words one-by-one:")

    splitter = WordSplitter(sentence)

    for word in splitter:
        print(word)
