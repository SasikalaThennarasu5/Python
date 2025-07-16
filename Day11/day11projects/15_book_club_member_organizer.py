club1 = {"Alice", "Bob", "Charlie"}
club2 = {"Charlie", "Daisy"}

common = club1 & club2
exclusive = club1 ^ club2

print("Common members:", common)
print("Exclusive members:", exclusive)