responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "what is your name": "I'm PyBot.",
    "bye": "Goodbye!"
}

while True:
    msg = input("You: ").strip().lower()
    if msg in responses:
        print("Bot:", responses[msg])
        if msg == "bye": break
    else:
        print("Bot: I don't understand.")
