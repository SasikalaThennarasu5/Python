import time

def chatbot_typing(message, delay=0.1):
    """
    Generator that yields one character at a time from the message.
    Supports interruption using send().
    """
    for char in message:
        # If user sends 'skip', yield entire message remaining at once
        interrupt = yield char
        if interrupt == "skip":
            yield message[message.index(char)+1:]
            return
        time.sleep(delay)

def simulate_chatbot_response(message):
    print(" Chatbot is typing...\n")
    typing_gen = chatbot_typing(message)
    
    try:
        while True:
            char = next(typing_gen)
            print(char, end='', flush=True)
            time.sleep(0.01)  # Slight buffer for console render

    except StopIteration:
        print("\n Chatbot finished typing.")

def main():
    message = "Hello! I hope you're having a great day. Let me know if I can help you with anything!"
    typing_gen = chatbot_typing(message)

    print(" Chatbot is typing (Press Enter to continue typing or type 'skip' to skip)...\n")
    
    try:
        while True:
            user_input = input("🔹Press Enter or type 'skip': ").strip().lower()
            try:
                if user_input == "skip":
                    result = typing_gen.send("skip")
                    print(result)
                    break
                else:
                    print(next(typing_gen), end='', flush=True)
            except StopIteration:
                break

    except KeyboardInterrupt:
        print("\n Interrupted.")

if __name__ == "__main__":
    main()
