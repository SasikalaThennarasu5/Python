
def print_report_card(student):
    roll_no, name = student["info"]
    print(f"\nReport Card for {name} (Roll No: {roll_no})")
    for subject, grade in student["grades"].items():
        print(f"  {subject}: {grade}")
    avg = student.get("average", "N/A")
    print(f"  Average: {avg:.2f}" if isinstance(avg, float) else f"  Average: {avg}")
