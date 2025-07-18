from .exceptions import InvalidMarkError, EmptyMarksError

def validate_marks(marks):
    if not marks:
        raise EmptyMarksError("No marks provided.")
    for m in marks:
        if m < 0 or m > 100:
            raise InvalidMarkError(f"Invalid mark found: {m}")
    return True

def calculate_average(marks):
    validate_marks(marks)
    return sum(marks) / len(marks)
