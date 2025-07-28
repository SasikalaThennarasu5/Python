import json
import random

class AdventureGame:
    def __init__(self, save_file='adventure_save.json'):
        self.rooms = {
            "village": {
                "desc": "You are in a peaceful village. A road leads north.",
                "exits": {"north": "forest"}
            },
            "forest": {
                "desc": "You enter a dark forest. The path leads east to the mountains or south to the village.",
                "exits": {"east": "mountains", "south": "village"},
                "enemy": "wild boar"
            },
            "mountains": {
                "desc": "You are in the rocky mountains. A mysterious cave lies ahead.",
                "exits": {"west": "forest", "up": "cave"},
                "item": "magic gem"
            },
            "cave": {
                "desc": "The cave is quiet... too quiet. You feel something is watching.",
                "exits": {"down": "mountains"},
                "enemy": "dragon"
            }
        }
        self.current_room = "village"
        self.inventory = []
        self.hp = 100
        self.save_file = save_file
        self.game_over = False
        self.ending_shown = False

    def describe(self):
        room = self.rooms[self.current_room]
        print(f"\n{room['desc']}")
        if "item" in room:
            print(f"You see a {room['item']} here.")
        if "enemy" in room:
            print(f"A {room['enemy']} blocks your path!")
            self.combat(room["enemy"])

    def move(self, direction):
        if direction in self.rooms[self.current_room]["exits"]:
            self.current_room = self.rooms[self.current_room]["exits"][direction]
            self.describe()
        else:
            print("You can't go that way.")

    def combat(self, enemy):
        enemy_hp = random.randint(30, 60)
        print(f"\nCombat with {enemy} begins!")
        while enemy_hp > 0 and self.hp > 0:
            action = input("Attack or Run? (a/r): ").lower()
            if action == "a":
                dmg = random.randint(10, 20)
                enemy_hp -= dmg
                print(f"You hit the {enemy} for {dmg} damage.")
                if enemy_hp <= 0:
                    print(f"You defeated the {enemy}!")
                    del self.rooms[self.current_room]["enemy"]
                    break
                edmg = random.randint(5, 15)
                self.hp -= edmg
                print(f"The {enemy} hits you for {edmg}. HP: {self.hp}")
            elif action == "r":
                print("You fled back to the previous room.")
                self.move("down" if "down" in self.rooms[self.current_room]["exits"] else "south")
                return
        if self.hp <= 0:
            print("You have died in battle.")
            self.game_over = True

    def take_item(self):
        room = self.rooms[self.current_room]
        if "item" in room:
            item = room.pop("item")
            self.inventory.append(item)
            print(f"You picked up {item}.")
        else:
            print("No item to take.")

    def show_inventory(self):
        print("Inventory:", self.inventory)

    def save_game(self):
        data = {
            "current_room": self.current_room,
            "inventory": self.inventory,
            "hp": self.hp,
            "rooms": self.rooms
        }
        with open(self.save_file, "w") as f:
            json.dump(data, f)
        print("Game saved.")

    def load_game(self):
        try:
            with open(self.save_file, "r") as f:
                data = json.load(f)
                self.current_room = data["current_room"]
                self.inventory = data["inventory"]
                self.hp = data["hp"]
                self.rooms = data["rooms"]
            print("Game loaded successfully.")
        except FileNotFoundError:
            print("No saved game found.")

    def check_endings(self):
        if self.hp <= 0 and not self.ending_shown:
            print("☠️ Ending: You died. Evil has prevailed.")
            self.ending_shown = True
            self.game_over = True
        elif "magic gem" in self.inventory and self.current_room == "village" and not self.ending_shown:
            print("🏆 Ending: You brought back the magic gem. Peace returns to the land.")
            self.ending_shown = True
            self.game_over = True
        elif "magic gem" not in self.inventory and self.current_room == "village" and not self.ending_shown:
            print("❓ Ending: You returned home empty-handed. The world remains in danger.")
            self.ending_shown = True
            self.game_over = True

# Game Loop
if __name__ == "__main__":
    game = AdventureGame()
    game.load_game()
    game.describe()

    while not game.game_over:
        print("\n--- Options ---")
        print("1. Move")
        print("2. Take Item")
        print("3. Inventory")
        print("4. Save Game")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == '1':
            direction = input("Which direction? (north/south/east/west/up/down): ").lower()
            game.move(direction)
            game.check_endings()
        elif choice == '2':
            game.take_item()
        elif choice == '3':
            game.show_inventory()
        elif choice == '4':
            game.save_game()
        elif choice == '5':
            print("Quitting game.")
            break
