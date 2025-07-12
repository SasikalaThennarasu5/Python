books = ["Python Basics", "Machine Learning", "Data Structures"]
borrowed = []

def borrow_book():
    show_books()
    book = input("Enter book name to borrow: ")
    if book in books:
        books.remove(book)
        borrowed.append(book)
        print("Book borrowed.")
    else:
        print("Not available.")

def return_book():
    book = input("Enter book name to return: ")
    if book in borrowed:
        borrowed.remove(book)
        books.append(book)
        print("Book returned.")
    else:
        print("You don't have this book.")

def show_books():
    print("Available books:")
    for b in books:
        print("-", b)

while True:
    print("\n1. Borrow\n2. Return\n3. Show Books\n4. Exit")
    ch = input("Choose: ")
    if ch == '1': borrow_book()
    elif ch == '2': return_book()
    elif ch == '3': show_books()
    elif ch == '4': break
    else: print("Invalid")