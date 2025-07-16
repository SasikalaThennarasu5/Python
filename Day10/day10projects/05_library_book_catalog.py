# 5. Library Book Catalog

books = {
    1: {"title": "Python", "author": "John", "copies": 3},
    2: {"title": "Java", "author": "Mike", "copies": 1}
}

# Add book
books[3] = {"title": "C++", "author": "Sam", "copies": 2}

# Borrow
books[1]["copies"] -= 1

# Return
books[1]["copies"] += 1

# Delete if zero
for id in list(books.keys()):
    if books[id]["copies"] == 0:
        books.pop(id)

# Display
for id, info in books.items():
    print(f"{info['title']} - Copies: {info['copies']}")