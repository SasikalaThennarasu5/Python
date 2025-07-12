def count_words(text):
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return len(words), freq

text = input("Enter paragraph: ")
total, frequencies = count_words(text)
print(f"Total words: {total}")
for word, count in frequencies.items():
    print(f"{word}: {count}")
