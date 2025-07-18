from student_utils import enrollment, course_manager

def main():
    while True:
        print("\n--- Student Enrollment System ---")
        print("1. Add Student")
        print("2. Enroll Course")
        print("3. View Student Info")
        print("4. List All Students")
        print("5. List Available Courses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            sid = int(input("Enter student ID: "))
            student_id = (sid,)  # tuple
            enrollment.add_student(student_id, name)

        elif choice == '2':
            sid = int(input("Enter student ID: "))
            student_id = (sid,)
            course = input("Enter course to enroll: ")

            if course_manager.is_course_available(course):
                enrollment.enroll_course(student_id, course)
            else:
                print("Invalid course name.")

        elif choice == '3':
            sid = int(input("Enter student ID: "))
            student_id = (sid,)
            info = enrollment.get_student_info(student_id)
            if info:
                print(f"Name: {info['name']}")
                print(f"Enrolled Courses: {', '.join(info['courses']) or 'None'}")
            else:
                print("Student not found.")

        elif choice == '4':
            all_students = enrollment.list_students()
            for sid, data in all_students.items():
                print(f"ID: {sid[0]}, Name: {data['name']}, Courses: {', '.join(data['courses']) or 'None'}")

        elif choice == '5':
            print("Available Courses:", ', '.join(course_manager.list_courses()))

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
