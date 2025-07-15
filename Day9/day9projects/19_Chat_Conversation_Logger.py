# Project 19: Chat Conversation Logger
messages = [
    ("10:00", ("Alice", "Hello")),
    ("10:05", ("Bob", "Hi")),
    ("10:10", ("Alice", "How are you?"))
]

for time, (sender, msg) in messages:
    print(f"[{time}] {sender}: {msg}")