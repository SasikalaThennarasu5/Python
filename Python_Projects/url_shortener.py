
import json
import string
import random

def cache(func):
    cached_urls = {}
    def wrapper(*args, **kwargs):
        key = args[0]
        if key in cached_urls:
            print("Returning cached short URL.")
            return cached_urls[key]
        result = func(*args, **kwargs)
        cached_urls[key] = result
        return result
    return wrapper

def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class URLShortener:
    def __init__(self):
        self.url_map = {}

    @cache
    def shorten(self, long_url):
        if not long_url.startswith("http"):
            raise ValueError("Invalid URL format")
        shortcode = generate_shortcode()
        self.url_map[shortcode] = long_url
        return shortcode

    def redirect(self, shortcode):
        return self.url_map.get(shortcode, "URL not found.")

    def delete(self, shortcode):
        if shortcode in self.url_map:
            del self.url_map[shortcode]
            return True
        return False

    def list_urls(self):
        for code, url in self.url_map.items():
            print(f"{code} -> {url}")

    def save_to_file(self, filename="urls.json"):
        with open(filename, "w") as file:
            json.dump(self.url_map, file)

    def load_from_file(self, filename="urls.json"):
        try:
            with open(filename, "r") as file:
                self.url_map = json.load(file)
        except FileNotFoundError:
            self.url_map = {}

    def expired_urls(self):
        for code in self.url_map:
            if code.endswith("X"):  # Just a mock rule for expiration
                yield code

# Example usage
if __name__ == "__main__":
    shortener = URLShortener()
    shortener.load_from_file()
    url = "http://example.com"
    try:
        code = shortener.shorten(url)
        print(f"Shortened URL code: {code}")
    except ValueError as e:
        print(e)
    print(shortener.redirect(code))
    shortener.list_urls()
    shortener.save_to_file()
