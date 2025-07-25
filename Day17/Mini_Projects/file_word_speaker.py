import string

def word_by_word_reader(filename):
    """
    Lazily yields one word at a time from the given file,
    simulating word-by-word audio playback.
    Punctuation is stripped and memory usage is minimal.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove punctuation, split into words
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.strip().split()
            for word in words:
                yield word

if __name__ == "__main__":
    for word in word_by_word_reader("sample_paragraph.txt"):
        print(f" {word}")
