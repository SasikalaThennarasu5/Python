from recipe_io import *

add_recipe("Pasta", ["noodles", "sauce"], ["boil", "mix"], "Italian")
add_recipe("Tea", ["water", "tea leaves"], ["boil", "steep"], "Beverage")

print("All Recipes:", list_all())
print("With 'water':", search_by_ingredient("water"))