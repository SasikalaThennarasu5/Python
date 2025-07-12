def count_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

sentence = input("Enter a sentence: ")
freq_map = count_frequency(sentence)
for char, count in freq_map.items():
    print(f"'{char}': {count}")
