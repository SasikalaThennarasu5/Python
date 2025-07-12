# Movie Watchlist App

watchlist = ["Inception", "Interstellar", "Parasite", "Dune", "Oppenheimer", "Tenet"]

# Mark watched
watchlist.remove("Dune")

# Show top 5
print("Top 5 movies to watch:", watchlist[:5])

# Display with index
print("\nWatchlist:")
for idx, movie in enumerate(watchlist):
    print(f"{idx+1}. {movie}")
