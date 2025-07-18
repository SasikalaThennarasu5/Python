# grocery/checkout.py

import json
import random
from datetime import datetime
from grocery.cart import cart
from grocery.items import GROCERY_ITEMS

def generate_bill():
    if not cart:
        print("Cart is empty. Cannot proceed to checkout.")
        return

    bill_id = f"BILL{random.randint(1000,9999)}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum(GROCERY_ITEMS[item] * qty for item, qty in cart.items())

    bill_data = {
        "bill_id": bill_id,
        "timestamp": timestamp,
        "items": [
            {"item": item, "quantity": qty, "price_per_unit": GROCERY_ITEMS[item], "total": GROCERY_ITEMS[item]*qty}
            for item, qty in cart.items()
        ],
        "total_amount": total
    }

    filename = f"{bill_id}.json"
    with open(filename, "w") as f:
        json.dump(bill_data, f, indent=4)

    print(f"\n✅ Bill Generated! ID: {bill_id}")
    print(f"🕒 Time: {timestamp}")
    print(f"💰 Total Amount: ₹{total}")
    print(f"🧾 Bill saved to: {filename}")
