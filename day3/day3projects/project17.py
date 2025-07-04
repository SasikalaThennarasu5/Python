#  17. Basic Chat Filter App
banned_words = ["bad", "hate", "spam"]
msg = input("Enter your message: ").lower()
if any(word in msg for word in banned_words):
    print("Warning: Message contains banned words!")
else:
    print("Message sent successfully.")