import sys
import time
import re
import unittest

# 1. Compare list vs generator for 10 million numbers
def list_vs_generator_benchmark():
    N = 10_000_000

    # List comprehension
    start_list = time.time()
    lst = [i for i in range(N)]
    list_sum = sum(lst)
    end_list = time.time()
    list_memory = sys.getsizeof(lst)

    # Generator expression
    start_gen = time.time()
    gen = (i for i in range(N))
    gen_sum = sum(gen)
    end_gen = time.time()
    gen_memory = sys.getsizeof(gen)

    return {
        "list_time": round(end_list - start_list, 2),
        "gen_time": round(end_gen - start_gen, 2),
        "list_memory": list_memory,
        "gen_memory": gen_memory,
        "list_sum": list_sum,
        "gen_sum": gen_sum
    }

# 2. Use map() to transform each value in a generator
def num_generator():
    for i in range(1, 6):
        yield i

# 3. Generator pipeline
def gen_numbers():
    for i in range(10):
        yield i

def filter_even(gen):
    for i in gen:
        if i % 2 == 0:
            yield i

def square(gen):
    for i in gen:
        yield i * i

# 4. Simulate reading user commands (mock input)
def user_input_simulator(commands):
    for cmd in commands:
        yield cmd

# 5. Generator that filters valid email addresses
def valid_email_generator(emails):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    for email in emails:
        if re.match(pattern, email):
            yield email

# ----------------- UNIT TEST FOR EMAIL VALIDATOR -----------------
class TestEmailGenerator(unittest.TestCase):
    def test_valid_email_generator(self):
        input_emails = [
            "test@example.com",
            "invalid-email",
            "hello@world.co",
            "@missing.com",
            "john.doe@gmail"
        ]
        result = list(valid_email_generator(input_emails))
        expected = ["test@example.com", "hello@world.co"]
        self.assertEqual(result, expected)

# ---------------------- RUN Tasks ----------------------
if __name__ == "__main__":
    # 1. Benchmark
    print("1. Benchmark: List vs Generator (10 million)")
    result = list_vs_generator_benchmark()
    print(result, "\n")

    # 2. map() with generator
    print("2. map() with generator (double):", list(map(lambda x: x * 2, num_generator())))

    # 3. Generator pipeline: numbers → even → squares
    print("3. Generator pipeline output:", list(square(filter_even(gen_numbers()))))

    # 4. Simulate user input
    print("4. Simulated user inputs:")
    for cmd in user_input_simulator(["login", "view", "logout"]):
        print("Command:", cmd)

    # 5. Unit test for email filtering generator
    print("\n5. Running unit test for email filtering:")
    unittest.main(argv=[''], exit=False)
