
from journal.entry import new_entry
from journal.viewer import view_entries
from journal.exporter import export_all

def menu():
    while True:
        print("\n1. New Entry\n2. View Entries\n3. Search Entries\n4. Export All\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            new_entry()
        elif choice == "2":
            date = input("Date (YYYY-MM-DD, leave blank for all): ").strip() or None
            view_entries(date)
        elif choice == "3":
            keyword = input("Keyword: ")
            view_entries(keyword=keyword)
        elif choice == "4":
            export_all()
            print("Exported to 'journal_export.txt'.")
        elif choice == "5":
            break

if __name__ == "__main__":
    menu()
