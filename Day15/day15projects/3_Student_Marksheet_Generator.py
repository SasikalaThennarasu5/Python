class InvalidMarkError(Exception): pass

def generate_marksheet(students):
    for student in students:
        try:
            name, marks = student['name'], student['marks']
            for subject, mark in marks.items():
                if mark < 0: raise ValueError("Negative mark")
                if mark > 100: raise InvalidMarkError("Mark > 100")
        except Exception as e:
            print(f"Skipping {name}: {e}")
        else:
            print(f"{name}'s marks recorded.")
        finally:
            print("Processed student")