import re
from .catalog import list_ebooks

def search_ebooks(keyword):
    ebooks = list_ebooks()
    pattern = re.compile(keyword, re.IGNORECASE)
    results = [book for book in ebooks if pattern.search(os.path.basename(book))]
    return results
