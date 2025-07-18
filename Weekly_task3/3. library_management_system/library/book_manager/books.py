# Handles book storage and retrieval

book_db = {}

def add_book(isbn, title, author, genre):
    book_db[isbn] = {
        'title': title,
        'author': author,
        'genre': genre
    }

def get_book(isbn):
    return book_db.get(isbn, None)

def list_books():
    return book_db
