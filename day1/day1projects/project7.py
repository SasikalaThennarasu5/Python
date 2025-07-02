# 7. Movie Organizer
movie1 = input("Enter favorite movie 1: ")
movie2 = input("Enter favorite movie 2: ")
movie3 = input("Enter favorite movie 3: ")
movies = (movie1, movie2, movie3)
print("\n🎬 Favorite Movies:", movies)
for movie in movies:
    print("Movie:", movie)
print("Type of movies variable:", type(movies))