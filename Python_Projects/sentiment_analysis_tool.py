from textblob import TextBlob

def cache_results(func):
    cache = {}
    def wrapper(text):
        if text in cache:
            return cache[text]
        result = func(text)
        cache[text] = result
        return result
    return wrapper

class Analyzer:
    def __init__(self):
        pass

    @cache_results
    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        return sentiment, polarity

if __name__ == "__main__":
    analyzer = Analyzer()
    while True:
        text = input("Enter text to analyze (or 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        sentiment, score = analyzer.analyze_sentiment(text)
        print(f"Sentiment: {sentiment} (Score: {score:.2f})\n")
