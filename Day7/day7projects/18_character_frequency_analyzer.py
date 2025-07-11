text = input("Enter a sentence: ").lower()
vowels = "aeiou"
for v in vowels:
    print(f"{v}: {text.count(v)}")