# Project 14: Alphabet Counter
print("\nProject 14: Alphabet Counter")
text = "Python@123 is Great!"
vowels = consonants = digits = specials = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        specials += 1
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Specials: {specials}")