# Student Score Tracker

students = [["Ram", 85], ["Sam", 78]]

# Update score
students[1][1] = 82

# Add student
students.append(["Anu", 91])

# Remove student
students.remove(["Ram", 85])

# Display all
print("Students and scores:")
for name, score in students:
    print(f"{name}: {score}")

# Sort by score descending
students.sort(key=lambda x: x[1], reverse=True)
print("\nTop scorer:", students[0])
