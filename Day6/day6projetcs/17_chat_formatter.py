# Chat Formatter
def format_chats(*msgs):
    return list(map(lambda m: f"[10:00AM] {m.capitalize()}", msgs))

print("Formatted:", format_chats("hello", "how are you?", "great!"))
