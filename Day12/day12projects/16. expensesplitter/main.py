# expensesplitter/main.py

from expensesplitter import members, split, report

def main():
    while True:
        print("\n--- Expense Splitter Menu ---")
        print("1. Add Member")
        print("2. List Members")
        print("3. Add Expense")
        print("4. Show Report")
        print("5. Export Report (CSV)")
        print("6. Exit")

        choice = input("Choose an option (1–6): ")

        if choice == "1":
            name = input("Enter member name: ")
            members.add_member(name)
        elif choice == "2":
            members.list_members()
        elif choice == "3":
            payer = input("Who paid? ")
            amount = input("Amount paid: ")
            reason = input("Reason for expense: ")
            split.add_expense(payer, amount, reason)
        elif choice == "4":
            report.show_report()
        elif choice == "5":
            report.export_report()
        elif choice == "6":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
