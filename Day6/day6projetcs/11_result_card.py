# Result Card Generator
def generate_result(**kwargs):
    grades = list(map(lambda m: "A" if m >= 90 else "B" if m >= 75 else "C" if m >= 50 else "F", kwargs.values()))
    total = sum(kwargs.values())
    avg = total / len(kwargs)
    status = "Pass" if all(m >= 35 for m in kwargs.values()) else "Fail"
    return total, avg, grades, status

print(generate_result(Math=90, English=70, Science=80, History=60))
