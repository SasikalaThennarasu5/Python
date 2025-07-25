class CircularPlaylist:
    def __init__(self, songs):
        if not songs:
            raise ValueError("Playlist cannot be empty.")
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        song = self.songs[self.index]
        self.index = (self.index + 1) % len(self.songs)  # Wrap around
        return song


# ---  Usage ---
if __name__ == "__main__":
    playlist = ["Song A", "Song B", "Song C", "Song D"]
    circular_iter = CircularPlaylist(playlist)

    print("🎵 Circular Playlist (10 songs):")
    for _ in range(10):  # Stop after 10 iterations
        print(next(circular_iter))
