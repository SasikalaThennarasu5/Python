import os
import requests
from PIL import Image
from io import BytesIO

class Downloader:
    def __init__(self, url_list):
        self.url_list = url_list
        self.download_dir = "downloaded_images"
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def is_valid_url(self, url):
        return url.startswith("http")

    def save_image(self, image, filename):
        path = os.path.join(self.download_dir, filename)
        image.save(path)
        return path

    def download_images(self):
        for i, url in enumerate(self.url_list):
            try:
                if not self.is_valid_url(url):
                    raise ValueError("Invalid URL")
                response = requests.get(url)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
                filename = f"image_{i+1}.{img.format.lower()}"
                yield self.save_image(img, filename)
            except Exception as e:
                print(f"Failed to download {url}: {e}")

# Example usage
if __name__ == "__main__":
    urls = [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/300"
    ]
    downloader = Downloader(urls)
    for path in downloader.download_images():
        print(f"Downloaded: {path}")
