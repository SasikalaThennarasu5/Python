class InvalidCategoryError(Exception): pass

def track_expense(expenses):
    total = 0
    try:
        for item in expenses:
            if item['category'] not in ['Food', 'Travel']:
                raise InvalidCategoryError("Bad category")
            total += float(item['amount'])
    except Exception as e:
        print(e)
    finally:
        print("Total:", total)