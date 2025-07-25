def email_sender(emails):
    """Generator to yield emails one by one with dynamic batch control and error simulation."""
    sent_count = 0
    batch_size = 1
    total = len(emails)

    try:
        while sent_count < total:
            for _ in range(batch_size):
                if sent_count >= total:
                    break
                try:
                    email = emails[sent_count]
                    yield email  # Yield the current email
                    sent_count += 1
                except Exception as e:
                    print(f"[ERROR] Failed to send to {email}: {e}")
            batch_size = yield  # Pause and wait for new batch size
    except GeneratorExit:
        print("[INFO] Generator closed.")
    except Exception as e:
        print(f"[EXCEPTION] {e}")
    finally:
        return f"[DONE] All {sent_count} emails processed."

# Example usage
if __name__ == "__main__":
    email_list = [
        "user1@example.com",
        "user2@example.com",
        "user3@example.com",
        "fail@example.com",
        "user4@example.com",
        "user5@example.com"
    ]

    gen = email_sender(email_list)

    try:
        # Start generator and get first email
        print("[STARTING EMAIL SEND]")
        email = next(gen)
        print(f" Sent to: {email}")

        # Simulate batch sending with pauses and batch size change
        while True:
            try:
                # Send 2 emails in next batch
                email = gen.send(2)
                print(f" Sent to: {email}")

                if email == "fail@example.com":
                    gen.throw(Exception("Simulated failure"))

            except StopIteration as done:
                print(done.value)  # Access return value from generator
                break

    except Exception as e:
        print(f"[OUTER EXCEPTION] {e}")
