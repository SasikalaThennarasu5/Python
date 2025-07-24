def get_grade():
    try:
        mark = int(input("Enter mark: "))
        assert 0 <= mark <= 100
        print("Valid mark:", mark)
        return 1
    except ValueError:
        print("Retry: Invalid input")
        return get_grade()
    finally:
        print("Attempt complete")

count = get_grade()