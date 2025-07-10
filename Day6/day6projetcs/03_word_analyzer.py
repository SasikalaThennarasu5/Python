# Word Analyzer Tool
def analyze_words(*words):
    lengths = list(map(len, words))
    upper_words = list(map(lambda w: w.upper(), words))
    freq_chars = [max(set(w), key=w.count) for w in words]
    return lengths, upper_words, freq_chars

data = analyze_words("hello", "banana", "apple")
print("Lengths:", data[0])
print("Uppercase:", data[1])
print("Most frequent chars:", data[2])
