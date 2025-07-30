
import json
import datetime

def log_chat(func):
    def wrapper(*args, **kwargs):
        user_input = args[1]
        with open("chat_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - USER: {user_input}\n")
        response = func(*args, **kwargs)
        with open("chat_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - BOT: {response}\n")
        return response
    return wrapper

class Chatbot:
    def __init__(self, response_file="responses.json"):
        try:
            with open(response_file, "r") as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            print("Response file not found. Loading default responses.")
            self.responses = {
                "hi": "Hello!",
                "bye": "Goodbye!",
                "how are you": "I'm just a bot, but I'm doing well!"
            }

    @log_chat
    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return self.responses[key]
        return "I'm sorry, I don't understand that."

    def chat(self):
        print("Chatbot: Hello! Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break
            print("Chatbot:", self.get_response(user_input))

if __name__ == "__main__":
    bot = Chatbot()
    bot.chat()
