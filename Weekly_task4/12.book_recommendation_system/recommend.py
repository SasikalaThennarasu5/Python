import random

def recommend_by_genre(books, genre):
    return [b for b in books if genre in b['genres']]

def recommend_by_author(books, author):
    return [b for b in books if b['author'] == author]
