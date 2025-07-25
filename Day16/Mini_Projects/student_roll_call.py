
class StudentRollIterator:
    def __init__(self, student_dict):
        self._students = list(student_dict.items())  # Convert to list of tuples (roll, name)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

if __name__ == "__main__":
    student_dict = {
        101: "Alice",
        102: "Bob",
        103: "Charlie",
        104: "David"
    }

    print(" Student Roll Call:")
    for roll, name in StudentRollIterator(student_dict):
        print(f"Roll No: {roll}, Name: {name}")
