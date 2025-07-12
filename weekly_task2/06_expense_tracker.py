expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").lower()
        expenses.append({'amount': amount, 'category': category})
        print("Expense added.")
    except ValueError:
        print("Invalid amount.")

def show_total():
    total = sum(e['amount'] for e in expenses)
    print(f"Total expenses: ${total:.2f}")

def show_by_category():
    categories = {}
    for e in expenses:
        categories[e['category']] = categories.get(e['category'], 0) + e['amount']
    for cat, amt in categories.items():
        print(f"{cat.capitalize()}: ${amt:.2f}")

while True:
    print("\n1. Add Expense\n2. Show Total\n3. Show by Category\n4. Exit")
    ch = input("Choose option: ")
    if ch == '1': add_expense()
    elif ch == '2': show_total()
    elif ch == '3': show_by_category()
    elif ch == '4': break
    else: print("Invalid choice.")
