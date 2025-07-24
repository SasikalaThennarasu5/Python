class InvalidResponseError(Exception): pass

def call_api():
    import random
    for _ in range(3):
        try:
            if random.choice([True, False]):
                raise TimeoutError("Timeout!")
            print("API Success")
            return
        except (TimeoutError, ConnectionError):
            print("Retrying...")
        finally:
            print("Attempt logged")