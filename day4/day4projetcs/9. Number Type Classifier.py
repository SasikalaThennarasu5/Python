# Project 9: Number Type Classifier
print("\nProject 9: Number Type Classifier")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Odd:", odd)
print("Even:", even)