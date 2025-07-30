
import json
import random
from functools import wraps

def repeat(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.current_index >= len(self.songs):
            self.current_index = 0
        return result
    return wrapper

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.current_index = 0

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f"Added: {song}")
        else:
            print(f"{song} already exists in playlist.")

    def shuffle(self):
        random.shuffle(self.songs)
        print("Playlist shuffled.")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "name": self.name,
                    "songs": self.songs,
                    "current_index": self.current_index
                }, f, indent=4)
            print("Playlist saved.")
        except Exception as e:
            print(f"Error saving playlist: {e}")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                playlist = Playlist(data["name"])
                playlist.songs = data["songs"]
                playlist.current_index = data["current_index"]
                print("Playlist loaded.")
                return playlist
        except Exception as e:
            print(f"Error loading playlist: {e}")
            return None

    @repeat
    def next_song(self):
        if not self.songs:
            return "No songs in playlist."
        song = self.songs[self.current_index]
        self.current_index += 1
        return song

# Example usage:
if __name__ == "__main__":
    p = Playlist("My Favorites")
    p.add_song("song1.mp3")
    p.add_song("song2.mp3")
    p.add_song("song3.mp3")
    p.shuffle()
    print(p.next_song())
    print(p.next_song())
    print(p.next_song())
    print(p.next_song())  # should repeat
    p.save_to_file("playlist.json")
    new_p = Playlist.load_from_file("playlist.json")
    if new_p:
        print(new_p.next_song())
