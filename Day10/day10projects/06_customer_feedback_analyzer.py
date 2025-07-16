feedbacks = {
    1: {"feedback": "good", "rating": 5},
    2: {"feedback": "bad", "rating": 2},
    3: {"feedback": "good", "rating": 4}
}

# Average rating
avg = sum(f["rating"] for f in feedbacks.values()) / len(feedbacks)
print("Average Rating:", avg)

# Count feedback types
summary = {}
for f in feedbacks.values():
    summary[f["feedback"]] = summary.get(f["feedback"], 0) + 1
print("Summary:", summary)

# Ratings > 4
high_rating = {k: v for k, v in feedbacks.items() if v["rating"] > 4}
print("High Ratings:", high_rating)