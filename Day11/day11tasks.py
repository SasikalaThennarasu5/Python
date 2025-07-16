#Creating and Accessing Sets
#01_create_fruit_set.py


favorite_fruits = {"apple", "banana", "mango", "orange"}
print(favorite_fruits)
#02_list_to_unique_set.py


fruits_list = ["apple", "banana", "apple", "orange", "banana"]
unique_fruits = set(fruits_list)
print(unique_fruits)
#03_check_item_in_set.py


colors = {"red", "green", "blue"}
print("green" in colors)
#04_set_from_string.py


unique_chars = set("hello world")
print(unique_chars)
#05_iterate_set.py


animals = {"cat", "dog", "elephant"}
for animal in animals:
    print(animal)
#✅ Adding Elements
#06_add_movies.py


movies = set()
movies.add("Inception")
movies.add("Avatar")
movies.add("Titanic")
movies.add("Matrix")
movies.add("Interstellar")
print(movies)
#07_update_subjects.py


subjects = {"Math", "English"}
subjects.update(["Biology", "Chemistry", "Physics"])
print(subjects)
#08_update_with_string.py


letters = set()
letters.update("science")
print(letters)
#✅ Removing Elements
#09_remove_city.py


cities = {"Delhi", "Mumbai", "Chennai"}
cities.remove("Mumbai")
print(cities)
#10_discard_city.py



cities = {"Delhi", "Mumbai"}
cities.discard("Kolkata")  # No error
print(cities)

#11_pop_random.py



colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining:", colors)

#12_clear_set.py

data = {"a", "b", "c"}
data.clear()
print("Is empty?", len(data) == 0)

#✅ Set Operations

#13_union_languages.py

set1 = {"Python", "Java"}
set2 = {"C++", "Python"}
print(set1.union(set2))

#14_intersection_sports.py

sports1 = {"Football", "Cricket"}
sports2 = {"Hockey", "Cricket"}
print(sports1.intersection(sports2))

#15_difference_sets.py

A = {1, 2, 3}
B = {2, 3, 4}
print(A - B)

#16_symmetric_difference.py

A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))

#17_chained_operations.py

A = {1, 2, 3}
B = {2, 3, 4}
result = (A | B) - (A & B)
print(result)

#✅ Set Relationships

#18_is_subset.py

backend = {"Node.js", "Express"}
fullstack = {"HTML", "CSS", "Node.js", "Express"}
print(backend.issubset(fullstack))

#19_is_superset.py

developers = {"Alice", "Bob", "Charlie"}
testers = {"Bob"}
print(developers.issuperset(testers))

#20_is_disjoint.py

colors1 = {"red", "blue"}
colors2 = {"green", "yellow"}
print(colors1.isdisjoint(colors2))

#21_multiple_subset_superset.py

A = {1, 2}
B = {1, 2, 3}
C = {4, 5}
print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint(C))

#22_required_courses.py

required = {"Python", "Git", "Data Structures"}
completed = {"Python", "Git", "Data Structures", "SQL"}
print(required.issubset(completed))

#✅ Working with copy()

#23_copy_set.py

original = {"pen", "pencil", "eraser"}
backup = original.copy()
backup.add("marker")
print("Original:", original)
print("Backup:", backup)

#✅ Frozen Set Tasks

#24_frozenset_vowels.py

vowels = frozenset("aeiou")
print(vowels)

#25_add_to_frozenset.py

vowels = frozenset("aeiou")
try:
    vowels.add("x")
except AttributeError as e:
    print("Error:", e)

#26_frozenset_dict_key.py

vowels = frozenset("aeiou")
cache = {vowels: "vowel_set"}
print(cache[vowels])

#✅ Set Comprehension

#27_even_numbers.py

evens = {x for x in range(1, 21) if x % 2 == 0}
print(evens)

#28_unique_lowercase.py

sentence = "Hello World, Python is FUN!"
unique = {char.lower() for char in sentence if char.isalpha()}
print(unique)

#29_squares.py

squares = {x ** 2 for x in range(1, 11)}
print(squares)

#30_filter_vowels.py

sentence = "Set operations are cool!"
vowels = "aeiou"
filtered = {char for char in sentence if char.lower() not in vowels}
print(filtered)

#✅ Real-World Simulations

#31_allowed_users.py

registered = {"alice", "bob", "carol"}
blocked = {"carol"}
allowed = registered - blocked
print(allowed)

#32_common_students.py

python = {"A", "B", "C"}
java = {"B", "C", "D"}
print(python & java)

#33_new_stocks.py

yesterday = {"AAPL", "GOOG"}
today = {"AAPL", "GOOG", "TSLA"}
print(today - yesterday)

#34_union_logged_in.py

yesterday = {"alice", "bob"}
today = {"bob", "carol"}
print(yesterday | today)

#35_password_changes.py

day1 = {"alice", "bob"}
day2 = {"bob", "dave"}
print(day1 ^ day2)

#36_detect_duplicates.py

skus = ["A1", "B2", "A1", "C3", "B2"]
unique = set(skus)
duplicates = len(skus) != len(unique)
print("Duplicates?", duplicates)

#37_unique_csv_column.py

import csv
unique_names = set()
with open("sample.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        unique_names.add(row['Name'])
print(len(unique_names))

#38_tag_manager.py


tags = set()
tags.update(["react", "python", "dev"])
tags.update(["openai", "python"])
print(tags)

#39_check_permissions.py

default_permissions = {"read", "write", "execute"}
requested = {"read", "write"}
print(requested.issubset(default_permissions))

#✅ Combination Tasks

#40_random_operations.py

import random
A = set(random.sample(range(1, 20), 5))
B = set(random.sample(range(10, 30), 5))
print("A:", A)
print("B:", B)
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

#41_contact_manager.py

emails = {"user1@example.com", "user2@example.com"}
emails.add("user3@example.com")
print(emails)

#42_achievements_tracker.py

player = {"WorldCup", "ChampionsLeague", "Olympics"}
majors = {"WorldCup", "Olympics"}
print(majors.issubset(player))

#43_unique_ips.py

logs = ["192.168.1.1", "192.168.1.2", "192.168.1.1"]
unique_ips = set(logs)
print(unique_ips)

#44_extract_hashtags.py

tweets = ["#fun #code", "#python", "#fun"]
hashtags = set()
for tweet in tweets:
    hashtags.update(word for word in tweet.split() if word.startswith("#"))
print(hashtags)

#45_unique_books.py

library1 = {"Book A", "Book B"}
library2 = {"Book C", "Book B"}
all_books = set()
all_books.update(library1, library2)
print(all_books)

#46_check_installed_modules.py

installed = {"numpy", "pandas", "matplotlib"}
required = {"numpy", "pandas"}
print(required.issubset(installed))

#✅ Edge Case Handling

#47_safe_remove.py

items = {"a", "b", "c"}
try:
    items.remove("x")
except KeyError:
    print("Item not found.")

#48_remove_vs_discard.py

s = {"x", "y"}
s.discard("z")  # No error
try:
    s.remove("z")
except KeyError:
    print("remove throws error if not found")

#49_remove_integers.py

mixed = {1, "a", 2, "b", 3.5, True}
no_ints = {item for item in mixed if not isinstance(item, int)}
print(no_ints)

#50_characters_from_text.py

text = """
Hello! Welcome to Python.
Sets are amazing, aren't they?
"""
import string
cleaned = {ch for ch in text if ch not in string.punctuation and not ch.isspace()}
print(cleaned)