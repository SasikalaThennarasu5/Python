branch1 = {"Book A", "Book B", "Book C"}
branch2 = {"Book B", "Book C", "Book D"}

all_books = branch1 | branch2
common_books = branch1 & branch2
only_branch1 = branch1 - branch2

print("All Books:", all_books)
print("Common Books:", common_books)
print("Only in Branch1:", only_branch1)