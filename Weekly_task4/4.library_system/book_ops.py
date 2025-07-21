
books = []

def add_book(title, author, year, genres):
    book = {
        "info": (title, author),
        "year": year,
        "genres": set(genres),
        "available": True
    }
    books.append(book)

def search_books(keyword):
    return [b for b in books if keyword.lower() in b["info"][0].lower() or keyword.lower() in b["info"][1].lower()]

def get_unique_genres():
    all_genres = set()
    for b in books:
        all_genres.update(b["genres"])
    return all_genres

def list_books():
    for b in books:
        title, author = b["info"]
        print(f"{title} by {author} - {'Available' if b['available'] else 'Borrowed'}")
