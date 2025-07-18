from students import register as student_register
from teachers import register as teacher_register
from subjects import assign as subject_assign

if __name__ == "__main__":
    # Example Usage
    student_register.register_student("Alice", 15, "S101")
    student_register.register_student("Bob", 14, "S102")

    teacher_register.register_teacher("Mrs. Smith", "Math", "T201")
    teacher_register.register_teacher("Mr. Brown", "Science", "T202")

    subject_assign.assign_subject("S101", "Math")
    subject_assign.assign_subject("S102", "Science")

    from students import report as student_report
    from teachers import report as teacher_report
    from subjects import report as subject_report

    print("\n--- Reports ---")
    student_report.generate_student_report()
    teacher_report.generate_teacher_report()
    subject_report.generate_subject_report()
