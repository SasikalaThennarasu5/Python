# Unique Word Counter
def analyze_text(text):
    words = text.split()
    return len(words), len(set(words)), max(words, key=len)

text = "This is a simple simple test paragraph"
print("Word Count:", analyze_text(text))
