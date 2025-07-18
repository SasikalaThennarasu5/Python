def get_grade_from_cgpa(cgpa):
    if cgpa >= 9:
        return "O"   # Outstanding
    elif cgpa >= 8:
        return "A+"
    elif cgpa >= 7:
        return "A"
    elif cgpa >= 6:
        return "B+"
    elif cgpa >= 5:
        return "B"
    elif cgpa >= 4:
        return "C"
    else:
        return "F"
