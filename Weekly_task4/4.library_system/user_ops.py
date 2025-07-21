
def borrow_book(books, title):
    for b in books:
        if b["info"][0].lower() == title.lower() and b["available"]:
            b["available"] = False
            print("Borrowed successfully")
            return
    print("Book not available or not found")

def return_book(books, title):
    for b in books:
        if b["info"][0].lower() == title.lower() and not b["available"]:
            b["available"] = True
            print("Returned successfully")
            return
    print("Book not found or not borrowed")
