def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

while True:
    word = input("Enter word/sentence: ")
    if is_palindrome(word):
        print("Palindrome!")
    else:
        print("Not a palindrome.")
    again = input("Check another? (y/n): ").lower()
    if again != 'y':
        break
