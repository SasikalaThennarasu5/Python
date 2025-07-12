movies = []

def add_movie():
    name = input("Enter movie name: ")
    try:
        rating = float(input("Enter rating (0-10): "))
        movies.append([name, rating])
    except ValueError:
        print("Invalid rating.")

def show_top_rated():
    if not movies:
        print("No movies yet.")
        return
    top = sorted(movies, key=lambda x: x[1], reverse=True)
    for m in top:
        print(f"{m[0]} - {m[1]}/10")

while True:
    print("\n1. Add Movie\n2. Show Top Rated\n3. Exit")
    ch = input("Choose: ")
    if ch == '1': add_movie()
    elif ch == '2': show_top_rated()
    elif ch == '3': break
    else: print("Invalid")
