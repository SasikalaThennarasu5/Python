from library.book_manager import books
from library.user_manager import users

def main():
    genres = set()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Get Book by ISBN")
        print("3. List All Books")
        print("4. List Available Genres")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            isbn1 = input("Enter ISBN part 1: ")
            isbn2 = input("Enter ISBN part 2: ")
            isbn = (isbn1, isbn2)
            books.add_book(isbn, title, author, genre)
            genres.add(genre)
            print(f"Book '{title}' added.")

        elif choice == '2':
            isbn1 = input("Enter ISBN part 1: ")
            isbn2 = input("Enter ISBN part 2: ")
            isbn = (isbn1, isbn2)
            book = books.get_book(isbn)
            if book:
                print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
            else:
                print("Book not found.")

        elif choice == '3':
            all_books = books.list_books()
            for isbn, data in all_books.items():
                print(f"ISBN: {isbn}, Title: {data['title']}, Author: {data['author']}, Genre: {data['genre']}")

        elif choice == '4':
            print("Available Genres:", ', '.join(genres) if genres else "None")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
