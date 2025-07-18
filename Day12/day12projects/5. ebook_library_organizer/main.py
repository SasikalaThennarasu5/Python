from . import catalog, search, reader

def main():
    print("=== eBook Library Organizer ===")
    while True:
        print("\nOptions:")
        print("1. List eBooks")
        print("2. Search eBook")
        print("3. Open eBook")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == '1':
            books = catalog.list_ebooks()
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
        elif choice == '2':
            term = input("Enter search term: ").strip()
            results = search.search_ebooks(term)
            if results:
                print("Results:")
                for r in results:
                    print(r)
            else:
                print("No matches found.")
        elif choice == '3':
            title = input("Enter title to open: ").strip()
            reader.open_ebook(title)
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
