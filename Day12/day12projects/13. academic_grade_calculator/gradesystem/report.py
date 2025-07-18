from .marks import calculate_average
from .grade import get_grade_from_cgpa

def generate_report(student_name, marks):
    cgpa = round(calculate_average(marks) / 10, 2)
    grade = get_grade_from_cgpa(cgpa)
    return {
        "name": student_name,
        "marks": marks,
        "CGPA": cgpa,
        "Grade": grade
    }
