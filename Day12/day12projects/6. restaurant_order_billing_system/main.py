from restaurant.menu import display_menu
from restaurant.order import Order
from restaurant.bill import calculate_bill

def main():
    print("Welcome to Python Restaurant")
    display_menu()

    order = Order()
    while True:
        try:
            item_id = int(input("\nEnter item number (0 to finish): "))
            if item_id == 0:
                break
            quantity = int(input("Enter quantity: "))
            order.add_item(item_id, quantity)
        except ValueError:
            print("Invalid input. Try again.")

    items = order.get_items()
    if not items:
        print("No items ordered.")
        return

    subtotal, tax, discount, grand_total = calculate_bill(items)

    print("\n\n====== BILL SUMMARY ======")
    print(f"Order ID: #{order.get_order_id()}")
    print("----------------------------")
    for item in items:
        print(f"{item['name']:15} x{item['quantity']} = ₹{item['total']:.2f}")
    print("----------------------------")
    print(f"{'Subtotal':20} ₹{subtotal:.2f}")
    print(f"{'Tax (5%)':20} ₹{tax:.2f}")
    print(f"{'Discount':20} -₹{discount:.2f}")
    print(f"{'Grand Total':20} ₹{grand_total:.2f}")
    print("============================")

if __name__ == "__main__":
    main()
