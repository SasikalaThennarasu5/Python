def order_processor(orders):
    """
    Lazily processes online orders using a generator.
    Supports pause/resume with send(), and returns a summary when complete.
    """
    processed = []
    paused = False
    index = 0

    while index < len(orders):
        # Check if paused
        if paused:
            control = yield " Paused"
            if control == "resume":
                paused = False
            continue

        # Yield next order
        order = orders[index]
        control = yield f" Processed order: {order}"
        processed.append(order)
        index += 1

        # Pause if instructed
        if control == "pause":
            paused = True

    return f"🎉 All {len(processed)} orders processed: {processed}"

# Example usage
if __name__ == "__main__":
    orders = ["Order #101", "Order #102", "Order #103", "Order #104"]
    processor = order_processor(orders)

    try:
        print(next(processor))  # Start processing

        print(processor.send(None))      # Process order 1
        print(processor.send("pause"))   # Pause after order 2
        print(processor.send(None))      # Show paused state
        print(processor.send("resume"))  # Resume processing
        print(processor.send(None))      # Process order 3
        print(processor.send(None))      # Process order 4

    except StopIteration as e:
        print(e.value)  # Final summary
