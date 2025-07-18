# Manages available courses

available_courses = {"Math", "Science", "History", "Computer Science", "Art"}

def is_course_available(course):
    return course in available_courses

def list_courses():
    return available_courses
