known_words = {"python", "data", "code"}
article = "Learn Python code and data science"
words = {word.lower() for word in article.split()}
unknown = words - known_words

print("Unknown words:", unknown)