
from pprint import pprint

grocery_items = []  # list of tuples (item, category)
bought_items = set()
categories = {}

def add_item(item, category):
    grocery_items.append((item, category))
    categories.setdefault(category, []).append(item)

def remove_item(item):
    global grocery_items
    grocery_items = [i for i in grocery_items if i[0] != item]
    for cat in categories:
        if item in categories[cat]:
            categories[cat].remove(item)

def mark_as_bought(item):
    bought_items.add(item)

def display_by_category():
    pprint(categories)

def search_item(keyword):
    result = [i for i, _ in grocery_items if keyword.lower() in i.lower()]
    pprint(result)
