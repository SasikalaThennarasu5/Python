admin = {"Alice", "Bob", "Charlie"}
editor = {"Alice", "Bob"}
viewer = {"Daisy"}

print("Is editor subset of admin?", editor.issubset(admin))
print("Is admin superset of editor?", admin.issuperset(editor))
print("Viewer and admin disjoint?", viewer.isdisjoint(admin))