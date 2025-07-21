from recommend import recommend_by_genre, recommend_by_author

books = [
    {'title': 'Python 101', 'author': 'John', 'genres': {'Tech', 'Programming'}},
    {'title': 'Gardening Basics', 'author': 'Jane', 'genres': {'Hobby', 'Nature'}},
]

print("Books by genre 'Tech':", recommend_by_genre(books, 'Tech'))
print("Books by author 'Jane':", recommend_by_author(books, 'Jane'))
