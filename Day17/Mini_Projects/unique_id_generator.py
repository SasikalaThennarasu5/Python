def unique_id_generator(prefix="TRX", start=1):
    """
    Infinite generator that yields unique IDs like TRX001, TRX002...
    Accepts reset point using send().
    Stops after 1000 IDs for demonstration.
    """
    count = start
    while count <= 1000:
        reset = yield f"{prefix}{count:03}"
        if reset is not None and isinstance(reset, int):
            count = reset
        else:
            count += 1
    raise StopIteration("🔚 Reached 1000 IDs - Stopping generator.")

# Demo usage
def main():
    generator = unique_id_generator()

    try:
        for _ in range(5):
            print(next(generator))  # TRX001 to TRX005

        print("\n Resetting ID to 500...\n")
        print(generator.send(500))  # TRX500
        print(next(generator))      # TRX501
        print(next(generator))      # TRX502

    except StopIteration as e:
        print(str(e))

if __name__ == "__main__":
    main()
