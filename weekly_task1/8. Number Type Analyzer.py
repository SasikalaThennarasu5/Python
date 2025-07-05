# Project 8: Number Type Analyzer
print("\\nProject 8: Number Type Analyzer")
nums = [-3, 4, 0, 7, -8]
for n in nums:
    typ = "Even" if n % 2 == 0 else "Odd"
    pos_neg = "Positive" if n > 0 else ("Negative" if n < 0 else "Zero")
    print(f"{n} is {typ} and {pos_neg}")