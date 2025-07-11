sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))