
import json
from functools import wraps

# Decorator for admin-only operations
def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("is_admin", False):
            print("Admin privileges required.")
            return
        return func(*args, **kwargs)
    return wrapper

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = Book(title, author)
        print(f"Book '{title}' added.")

    @admin_only
    def delete_book(self, title, **kwargs):
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' deleted.")
        else:
            print("Book not found.")

    def borrow_book(self, title):
        book = self.books.get(title)
        if book and book.available:
            book.available = False
            print(f"You have borrowed '{title}'.")
        elif book:
            print("Book is already borrowed.")
        else:
            print("Book not found.")

    def return_book(self, title):
        book = self.books.get(title)
        if book and not book.available:
            book.available = True
            print(f"You have returned '{title}'.")
        elif book:
            print("Book was not borrowed.")
        else:
            print("Book not found.")

    def search_book(self, title):
        return self.books.get(title, None)

    def list_available_books(self):
        for book in self:
            print(book)

    def list_overdue_books(self):  # Placeholder for demo
        print("This demo does not handle dates. Simulating one overdue book:")
        for title, book in self.books.items():
            if not book.available:
                print(f"'{title}' might be overdue.")

    def save_library(self, filename="library.json"):
        with open(filename, "w") as f:
            json.dump({title: vars(book) for title, book in self.books.items()}, f)
        print("Library saved.")

    def load_library(self, filename="library.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.books = {title: Book(**attrs) for title, attrs in data.items()}
            print("Library loaded.")
        except FileNotFoundError:
            print("Library file not found.")

    def __iter__(self):
        for book in self.books.values():
            if book.available:
                yield book

# Example usage
if __name__ == "__main__":
    lib = Library()
    lib.load_library()
    lib.add_book("1984", "George Orwell")
    lib.add_book("Brave New World", "Aldous Huxley")
    lib.borrow_book("1984")
    lib.return_book("1984")
    lib.list_available_books()
    lib.list_overdue_books()
    lib.delete_book("1984", is_admin=True)
    lib.save_library()
