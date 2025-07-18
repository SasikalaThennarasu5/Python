def say_hi():
    print("This runs in both import and direct execution.")

def test():
    print("Running test only when executed directly.")

if __name__ == "__main__":
    test()
