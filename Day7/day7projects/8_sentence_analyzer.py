sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("First space at index:", sentence.find(" "))
print("Total vowels:", sum(1 for c in sentence if c in vowels))
print("Total spaces:", sentence.count(" "))