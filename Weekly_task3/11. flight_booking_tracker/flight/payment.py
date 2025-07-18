# Handles payment processing

def process_payment(passenger_id, amount):
    # Dummy payment logic
    if amount <= 0:
        return f"Invalid amount for passenger {passenger_id}"
    return f"Payment of ₹{amount} successful for passenger {passenger_id}"
