# 17. College Course Registration

courses = {
    "Ravi": ["Math", "Science"],
    "Divya": ["English"],
}

# Add course
courses["Ravi"].append("History")

# Drop course
if "English" in courses["Divya"]:
    courses["Divya"].remove("English")

# Students in a course
course = "Math"
students = [s for s, c in courses.items() if course in c]
print("Students in Math:", students)
