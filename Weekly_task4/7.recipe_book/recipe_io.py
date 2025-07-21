recipes = {}

def add_recipe(name, ingredients, steps, category):
    recipes[name] = (ingredients, steps, category)

def delete_recipe(name):
    recipes.pop(name, None)

def search_by_ingredient(ingredient):
    return [name for name, (ing, _, _) in recipes.items() if ingredient in ing]

def list_all():
    return recipes.keys()