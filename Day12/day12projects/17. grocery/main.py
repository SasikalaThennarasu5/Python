# grocery/main.py

from grocery import items, cart, checkout

def main():
    while True:
        print("\n--- Grocery Shopping Menu ---")
        print("1. List Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            items.list_items()
        elif choice == "2":
            item = input("Enter item name: ").lower()
            try:
                qty = int(input("Enter quantity: "))
                cart.add_to_cart(item, qty)
            except ValueError:
                print("❌ Quantity must be a number.")
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            checkout.generate_bill()
        elif choice == "5":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
