import os
from .search import search_ebooks

def open_ebook(title):
    results = search_ebooks(title)
    if not results:
        print("No eBook found.")
        return
    print(f"Opening: {results[0]}")
    os.startfile(results[0]) if os.name == "nt" else os.system(f"open \"{results[0]}\"")
