import os
import pickle
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class Classifier:
    def __init__(self, model_path="spam_model.pkl", vectorizer_path="vectorizer.pkl"):
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.model = None
        self.vectorizer = None

    def preprocess(self, text):
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        return text.lower().split()

    def load_model(self):
        if not os.path.exists(self.model_path) or not os.path.exists(self.vectorizer_path):
            raise FileNotFoundError("Model or vectorizer not found.")
        with open(self.model_path, "rb") as f:
            self.model = pickle.load(f)
        with open(self.vectorizer_path, "rb") as f:
            self.vectorizer = pickle.load(f)

    def train(self, texts, labels):
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(texts)
        self.model = MultinomialNB()
        self.model.fit(X, labels)
        with open(self.model_path, "wb") as f:
            pickle.dump(self.model, f)
        with open(self.vectorizer_path, "wb") as f:
            pickle.dump(self.vectorizer, f)

    def predict(self, texts):
        if self.model is None or self.vectorizer is None:
            self.load_model()
        X = self.vectorizer.transform(texts)
        for label in self.model.predict(X):
            yield "Spam" if label else "Not Spam"

# Example usage
if __name__ == "__main__":
    clf = Classifier()

    # Example training (only run once)
    # texts = ["Free money!!!", "Hi, let's meet tomorrow", "You won a lottery!", "Hello friend"]
    # labels = [1, 0, 1, 0]
    # clf.train(texts, labels)

    try:
        predictions = clf.predict(["Congratulations, you won a prize!", "Meeting at 3pm today"])
        for result in predictions:
            print(result)
    except Exception as e:
        print("Error:", e)
