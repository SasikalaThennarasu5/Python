movies = {
    "Inception": {"ratings": [5, 4], "genre": "Sci-Fi"},
    "Up": {"ratings": [4], "genre": "Animation"}
}

# Add rating and update average
for m in movies:
    movies[m]["ratings"].append(5)
    movies[m]["avg_rating"] = sum(movies[m]["ratings"]) / len(movies[m]["ratings"])

# Sort
sorted_movies = sorted(movies.items(), key=lambda x: x[1]["avg_rating"], reverse=True)
print("Sorted:", sorted_movies)

# Filter by genre
filtered = {k: v for k, v in movies.items() if v["genre"] == "Sci-Fi"}
print(filtered)