source1 = {"Headline A", "Headline B"}
source2 = {"Headline B", "Headline C"}

duplicates = source1 & source2
unique = source1 | source2

print("Duplicates:", duplicates)
print("All Headlines:", unique)