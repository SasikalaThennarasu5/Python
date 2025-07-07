# 18. Palindrome Checker
# Scenario: Check if a word is a palindrome

# Input: word
word = input("Enter a word to check: ").strip().lower()

# Use for loop to reverse
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word  # prepend each character

# Use if to compare reversed and original
if word == reversed_word:
    result = " It is a Palindrome!"
else:
    result = " Not a Palindrome."

# Print if it's a palindrome
print("\n------ Palindrome Check Result ------")
print(f"Original Word : {word}")
print(f"Reversed Word : {reversed_word}")
print(f"Result        : {result}")
print("-------------------------------------")
