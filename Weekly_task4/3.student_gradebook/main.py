
from student_ops import *
from report_gen import *

def main():
    while True:
        print("\n1. Add Student 2. Update Grade 3. All Subjects 4. Topper 5. Report Cards 6. Exit")
        choice = input("Enter: ")

        if choice == "1":
            roll = input("Roll No: ")
            name = input("Name: ")
            add_student(roll, name)

        elif choice == "2":
            roll = input("Roll No: ")
            subj = input("Subject: ")
            grade = int(input("Grade: "))
            update_grades(roll, subj, grade)

        elif choice == "3":
            print("Subjects:", get_all_subjects())

        elif choice == "4":
            toppers = find_top_students()
            for t in toppers:
                print_report_card(t)

        elif choice == "5":
            calculate_averages()
            for s in students:
                print_report_card(s)

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
