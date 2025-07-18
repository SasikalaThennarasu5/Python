# expensesplitter/split.py

from decimal import Decimal, ROUND_HALF_UP
from expensesplitter.members import group_members

expenses = []

def add_expense(payer, amount, reason):
    if payer not in group_members:
        print("❌ Payer is not in the group.")
        return

    try:
        amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        share = (amount / len(group_members)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        split_data = {
            "payer": payer,
            "amount": amount,
            "reason": reason,
            "split": {member: (-share if member != payer else amount - share*(len(group_members)-1)) for member in group_members}
        }
        expenses.append(split_data)
        print(f"✅ Expense of ₹{amount} added for '{reason}'.")
    except:
        print("❌ Invalid amount.")
