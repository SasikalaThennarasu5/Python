# 19. Word Frequency Counter
# Scenario: Count frequency of characters in a word

# Input: a word
word = input("Enter a word: ").strip().lower()

# Use dictionary + for loop to count each character
frequency = {}

for char in word:
    # Use conditional logic to add/update count
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\n------ Character Frequency ------")
for char, count in frequency.items():
    print(f"'{char}' : {count}")
print("--------------------------------")
