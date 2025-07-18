# main.py

from recipe_book import add_recipe, display_recipes

def main():
    add_recipe("Pasta", ["noodles", "olive oil", "garlic", "cheese"], ["pan", "spoon", "strainer"])
    add_recipe("Salad", ["lettuce", "tomato", "olive oil", "salt"], ["bowl", "knife", "spoon"])
    add_recipe("Pasta", ["noodles", "butter", "cheese"], ["pot", "fork"])  # Duplicate title

    display_recipes()

if __name__ == "__main__":
    main()