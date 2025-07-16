available = {"salt", "sugar", "flour"}
required = {"flour", "eggs", "sugar"}

print("Can make recipe?", available.issuperset(required))
missing = required - available
print("Missing ingredients:", missing)