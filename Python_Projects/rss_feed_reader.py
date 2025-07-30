import feedparser
import time

def update_check(func):
    def wrapper(*args, **kwargs):
        print("Checking for updates...")
        return func(*args, **kwargs)
    return wrapper

class Feed:
    def __init__(self, url):
        self.url = url
        self.feed = feedparser.parse(url)

    @update_check
    def get_articles(self):
        for entry in self.feed.entries:
            yield {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published if "published" in entry else "No date"
            }

    def save_articles(self, filename="articles.txt"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for article in self.get_articles():
                    f.write(f"{article['title']}\n{article['link']}\n{article['published']}\n\n")
            print(f"Articles saved to {filename}")
        except Exception as e:
            print(f"Error saving articles: {e}")

if __name__ == "__main__":
    url = input("Enter RSS feed URL: ")
    feed = Feed(url)
    for article in feed.get_articles():
        print(f"{article['title']} ({article['published']})\n{article['link']}\n")
    save = input("Save articles to file? (y/n): ")
    if save.lower() == 'y':
        feed.save_articles()
