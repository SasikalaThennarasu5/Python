
from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m")
        return True
    except ValueError:
        return False

def is_valid_amount(amount_str):
    try:
        float(amount_str)
        return True
    except ValueError:
        return False
