import json
import random
from functools import wraps

def save_progress(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("game_save.json", "w") as f:
            json.dump(args[0].to_dict(), f)
        return result
    return wrapper

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def to_dict(self):
        return {"name": self.name, "health": self.health, "inventory": self.inventory}

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

class Scene:
    def __init__(self, scene_id, description, choices):
        self.scene_id = scene_id
        self.description = description
        self.choices = choices  # Dict of options

    def display(self):
        print(f"\nScene {self.scene_id}: {self.description}")
        for k, v in self.choices.items():
            print(f"{k}. {v['desc']}")

    def get_next_scene(self, choice):
        return self.choices.get(choice, {}).get("next")

    def get_action(self, choice):
        return self.choices.get(choice, {}).get("action")

def loot_generator():
    items = ["Sword", "Shield", "Potion", "Map"]
    for item in items:
        yield item

class Game:
    def __init__(self, player):
        self.player = player
        self.current_scene = "1"
        self.scenes = self.load_scenes()

    def load_scenes(self):
        return {
            "1": Scene("1", "You are at the start of your journey.", {
                "a": {"desc": "Go left into the forest", "next": "2"},
                "b": {"desc": "Go right toward the village", "next": "3"}
            }),
            "2": Scene("2", "A wild animal attacks you!", {
                "a": {"desc": "Fight", "next": "4", "action": self.fight},
                "b": {"desc": "Run", "next": "1"}
            }),
            "3": Scene("3", "You arrive at a quiet village.", {
                "a": {"desc": "Talk to the villagers", "next": "5"},
                "b": {"desc": "Search houses", "next": "6"}
            }),
            "4": Scene("4", "You won the fight!", {
                "a": {"desc": "Continue forward", "next": "7"}
            }),
            "5": Scene("5", "Villagers give you food and water.", {
                "a": {"desc": "Thank them and rest", "next": "1"}
            }),
            "6": Scene("6", "You found a hidden treasure!", {
                "a": {"desc": "Take the treasure", "next": "7", "action": self.loot}
            }),
            "7": Scene("7", "You reach the end of your adventure!", {})
        }

    def fight(self):
        print("Fighting...")
        self.player.take_damage(random.randint(5, 20))

    def loot(self):
        print("Looting...")
        gen = loot_generator()
        try:
            item = next(gen)
            print(f"You found a {item}!")
            self.player.add_to_inventory(item)
        except StopIteration:
            print("Nothing left to loot.")

    @save_progress
    def play(self):
        while self.current_scene:
            scene = self.scenes[self.current_scene]
            scene.display()
            choice = input("Choose an option: ").lower()
            action = scene.get_action(choice)
            if action:
                action()
            next_scene = scene.get_next_scene(choice)
            if next_scene:
                self.current_scene = next_scene
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    name = input("Enter your character's name: ")
    player = Player(name)
    game = Game(player)
    game.play()
