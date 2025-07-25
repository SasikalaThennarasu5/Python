
from typing import Generator

# Sample English to Tamil dictionary
eng_to_tamil = {
    "hello": "வணக்கம்",
    "world": "உலகம்",
    "apple": "ஆப்பிள்",
    "book": "புத்தகம்",
    "computer": "கணினி"
}

def lazy_translator(words: list) -> Generator[str, None, None]:
    """
    Lazily translates English words to Tamil.
    Yields both original and translated words, if available.
    """
    for word in words:
        word = word.lower().strip()
        if word in eng_to_tamil:
            yield word         # Yield original word
            yield eng_to_tamil[word]  # Then its translation
        else:
            yield f"[SKIPPED] '{word}' not in dictionary"

if __name__ == "__main__":
    word_list = ["Hello", "Book", "Tree", "World", "apple", "Rocket"]

    print(" Lazy Dictionary Translation:\n")
    translator = lazy_translator(word_list)
    for entry in translator:
        print(entry)
