
import json
from functools import wraps

# Decorator to log searches
def log_search(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Searching for recipes using {args[1]}...")
        return func(*args, **kwargs)
    return wrapper

# Recipe class
class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nSteps: {self.steps}"

# RecipeFinder class
class RecipeFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.recipes = self.load_recipes()

    def load_recipes(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return {name: Recipe(name, **details) for name, details in data.items()}
        except FileNotFoundError:
            return {}

    def save_recipes(self):
        with open(self.file_path, 'w') as f:
            json.dump({name: {"ingredients": recipe.ingredients, "steps": recipe.steps}
                      for name, recipe in self.recipes.items()}, f, indent=4)

    def add_recipe(self, name, ingredients, steps):
        self.recipes[name] = Recipe(name, ingredients, steps)
        self.save_recipes()
        print("Recipe added successfully.")

    @log_search
    def search_by_ingredient(self, ingredient):
        return (recipe for recipe in self.recipes.values() if ingredient in recipe.ingredients)

    def list_all_ingredients(self):
        unique_ingredients = set()
        for recipe in self.recipes.values():
            unique_ingredients.update(recipe.ingredients)
        return unique_ingredients


# Example usage
if __name__ == "__main__":
    finder = RecipeFinder("recipes.json")

    while True:
        print("\n--- Recipe Finder ---")
        print("1. Add Recipe")
        print("2. Search by Ingredient")
        print("3. List Unique Ingredients")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            ingredients = [i.strip() for i in ingredients]
            steps = input("Enter preparation steps: ")
            finder.add_recipe(name, ingredients, steps)

        elif choice == '2':
            ing = input("Enter ingredient to search for: ")
            found = finder.search_by_ingredient(ing)
            for recipe in found:
                print(recipe)

        elif choice == '3':
            ingredients = finder.list_all_ingredients()
            print("Unique ingredients:", ingredients)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Try again.")
