import winsound

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

def to_morse(text):
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            yield MORSE_CODE_DICT[char]

def play_morse(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(600, 200)
        elif symbol == '-':
            winsound.Beep(600, 500)
        elif symbol == '/':
            time.sleep(0.5)
        time.sleep(0.1)

def save_translation(text, morse):
    with open("translations.txt", "a") as f:
        f.write(f"{text} -> {morse}\n")

if __name__ == "__main__":
    message = input("Enter a message: ")
    morse_text = " ".join(to_morse(message))
    print("Morse Code:", morse_text)
    play_morse(morse_text)
    save_translation(message, morse_text)
