# Project 2: Vowel Counter App
print("\nProject 2: Vowel Counter App")
sentence = "This is a Sample Sentence"
vowel_count = 0
for ch in sentence:
    if ch.lower() in "aeiou":
        vowel_count += 1
print("Total Vowels:", vowel_count)