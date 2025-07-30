import requests
from bs4 import BeautifulSoup

def scrape(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all(['h1', 'h2', 'h3'])
        for tag in headlines:
            text = tag.get_text(strip=True)
            if text:
                yield {"title": text}
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    news_url = "https://www.bbc.com/news"
    for headline in scrape(news_url):
        print(headline)
