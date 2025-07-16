translator = {
    "hello": "வணக்கம்",
    "world": "உலகம்"
}

# Add/Update
translator["good"] = "நன்று"

# Delete
translator.pop("world", None)

# Search
print(translator.get("hello", "Not Found"))

# Reverse
rev = {v: k for k, v in translator.items()}
print(rev)