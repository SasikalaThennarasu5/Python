# Project 7: Vowel Remover Tool
print("\nProject 7: Vowel Remover Tool")
sentence = "Remove all vowels from this sentence"
result = ""
for ch in sentence:
    if ch.lower() in "aeiou":
        continue
    result += ch
print(result)