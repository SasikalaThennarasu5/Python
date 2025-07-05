# Project 20: Custom Size Multiplication Table
print("\nProject 20: Custom Size Multiplication Table")
size = 5
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()