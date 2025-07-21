students = [("001", "Alice"), ("002", "Bob")]
attendance = {}

def mark_attendance(date, present_students):
    attendance[date] = set(present_students)

def view_by_date(date):
    return attendance.get(date, set())