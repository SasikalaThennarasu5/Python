enrolled = {"Alice", "Bob", "Charlie"}
present = {"Alice", "Charlie"}

absentees = enrolled - present
present.add("Daisy")

print("Absentees:", absentees)
print("Updated Present:", present)