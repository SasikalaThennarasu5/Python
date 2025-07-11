text = input("Enter a paragraph: ").lower()
words = text.split()
unique_words = set(words)
for word in unique_words:
    print(f"{word}: {words.count(word)}")
print("Total number of words:", len(words))