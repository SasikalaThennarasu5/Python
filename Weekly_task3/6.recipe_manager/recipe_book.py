# recipe_book.py

# Dictionary to store recipes using (recipe title,) tuple as key
recipes = {}

# Set to store all utensils (avoiding duplicates)
utensils = set()

def add_recipe(title, ingredients_list, utensils_list):
    recipe_key = (title,)  # Tuple key
    if recipe_key in recipes:
        print(f"⚠️ Recipe '{title}' already exists.")
        return False

    recipes[recipe_key] = {
        "ingredients": ingredients_list,
        "utensils": set(utensils_list)  # Use set for utensils
    }

    utensils.update(utensils_list)
    print(f"✅ Recipe '{title}' added successfully.")
    return True

def display_recipes():
    print("\n🍽️ Recipe Book:")
    for recipe_key, details in recipes.items():
        print(f"\n📌 {recipe_key[0]}")
        print(f"Ingredients: {', '.join(details['ingredients'])}")
        print(f"Utensils: {', '.join(details['utensils'])}")
    print("\n🔧 All Unique Utensils Used:")
    print(", ".join(utensils))