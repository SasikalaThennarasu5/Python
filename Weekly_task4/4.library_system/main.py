
from book_ops import *
from user_ops import *

def main():
    while True:
        print("\n1. Add Book 2. Search 3. Borrow 4. Return 5. Genres 6. List Books 7. Exit")
        choice = input("Choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            genres = input("Genres (comma): ").split(",")
            add_book(title, author, year, genres)

        elif choice == "2":
            kw = input("Search keyword: ")
            results = search_books(kw)
            for b in results:
                print(f"{b['info'][0]} by {b['info'][1]}")

        elif choice == "3":
            t = input("Book title: ")
            borrow_book(books, t)

        elif choice == "4":
            t = input("Book title: ")
            return_book(books, t)

        elif choice == "5":
            print("Genres:", get_unique_genres())

        elif choice == "6":
            list_books()

        elif choice == "7":
            break

if __name__ == "__main__":
    main()
