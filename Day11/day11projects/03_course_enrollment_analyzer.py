python_students = {"Alice", "Bob", "Charlie"}
java_students = {"Bob", "Daisy", "Eve"}

both = python_students & java_students
only_python = python_students - java_students
all_students = python_students | java_students
exclusive = python_students ^ java_students

print("Both:", both)
print("Only Python:", only_python)
print("All:", all_students)
print("Exclusive:", exclusive)