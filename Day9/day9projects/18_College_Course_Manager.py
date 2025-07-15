# Project 18: College Course Manager
courses = [
    ("CS101", "Python", (4, "Dr. Smith")),
    ("CS102", "Java", (3, "Dr. Smith")),
    ("CS103", "DBMS", (2, "Dr. Lee"))
]

sorted_courses = sorted(courses, key=lambda x: x[2][0], reverse=True)
for cid, name, (credits, faculty) in sorted_courses:
    print(f"{cid} - {name} ({credits} credits) by {faculty}")