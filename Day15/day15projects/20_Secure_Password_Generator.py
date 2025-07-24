class WeakPasswordCriteriaError(Exception): pass

def generate_password(length):
    try:
        assert length >= 8
        import random, string
        chars = string.ascii_letters + string.digits + "!@#"
        pwd = ''.join(random.choice(chars) for _ in range(length))
        if not any(c in "!@#" for c in pwd):
            raise WeakPasswordCriteriaError("No special char")
        print("Password:", pwd)
    except Exception as e:
        print(e)
    finally:
        print("Password generation done")