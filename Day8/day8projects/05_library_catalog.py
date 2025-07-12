# Library Book Catalog

books = [["Atomic Habits", "James Clear"], ["1984", "George Orwell"], ["Dune", "Frank Herbert"]]

# Add book
books.append(["Sapiens", "Yuval Noah Harari"])

# Remove a book
books.remove(["1984", "George Orwell"])

# Update book title
books[0][0] = "Atomic Habits (Updated)"

# Search
search = "Dune"
for book in books:
    if search in book:
        print(f"Found: {book}")

# Recent additions
print("Recent:", books[-2:])
