def attendance(students, max_days):
    for s in students:
        try:
            if s['days'] > max_days:
                raise ValueError("Over max days")
            print(f"{s['name']} marked present")
        except Exception as e:
            print(f"Error: {e}")