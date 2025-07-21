
from grocery import *

def main():
    while True:
        print("\n1. Add 2. Remove 3. Bought 4. Display 5. Search 6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            item = input("Item: ")
            category = input("Category: ")
            add_item(item, category)

        elif choice == "2":
            item = input("Item to remove: ")
            remove_item(item)

        elif choice == "3":
            item = input("Item bought: ")
            mark_as_bought(item)

        elif choice == "4":
            print("Items by category:")
            display_by_category()

        elif choice == "5":
            keyword = input("Search: ")
            search_item(keyword)

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
