from pytube import YouTube

def progress_bar(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size * 100
    print(f"Downloading: {progress:.2f}% complete", end="\r")

class Downloader:
    def __init__(self, url):
        self.url = url
        self.yt = YouTube(url, on_progress_callback=progress_bar)

    def download(self, resolution="720p"):
        stream = self.yt.streams.filter(progressive=True, file_extension="mp4", res=resolution).first()
        if not stream:
            print("Desired resolution not available. Downloading the highest resolution.")
            stream = self.yt.streams.get_highest_resolution()
        stream.download()
        print(f"Downloaded: {self.yt.title}")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    yt_dl = Downloader(url)
    yt_dl.download()
