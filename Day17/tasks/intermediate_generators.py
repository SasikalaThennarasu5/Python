# 1. Generator yielding words one-by-one from a paragraph
def gen_words(paragraph):
    for word in paragraph.split():
        yield word

# 2. Generator yielding cumulative sum of numbers
def gen_cumulative_sum(nums):
    total = 0
    for num in nums:
        total += num
        yield total

# 3. Re-implement range using a generator
def custom_range(start, end, step=1):
    while start < end:
        yield start
        start += step

# 4. Generator to flatten a nested list
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# 5. Generator yielding factorials up to n
def gen_factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

# 6. Generator yielding powers of 2 up to a limit
def gen_powers_of_two(limit):
    value = 1
    while value <= limit:
        yield value
        value *= 2

# 7. Fibonacci sequence generator
def gen_fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# 8. Generator filtering only even numbers from a list
def gen_even_filter(lst):
    for num in lst:
        if num % 2 == 0:
            yield num

# 9. Chain two generators: numbers → squares
def gen_numbers(n):
    for i in range(n):
        yield i

def gen_squares_from_gen(gen):
    for num in gen:
        yield num * num

# 10. Reverse generator for a string
def reverse_string_gen(s):
    for ch in reversed(s):
        yield ch

# ---------------------- RUN EXAMPLES ----------------------
if __name__ == "__main__":
    print("1. Words in paragraph:")
    for word in gen_words("Python generators are powerful tools."):
        print(word, end=' ')
    print("\n")

    print("2. Cumulative sum:", list(gen_cumulative_sum([1, 2, 3, 4, 5])))

    print("3. Custom range 5 to 15:", list(custom_range(5, 15, 2)))

    print("4. Flatten nested list:")
    nested = [1, [2, [3, 4], 5], [6], 7]
    print(list(flatten(nested)))

    print("5. Factorials up to 5:", list(gen_factorials(5)))

    print("6. Powers of 2 up to 100:")
    print(list(gen_powers_of_two(100)))

    print("7. Fibonacci sequence up to 100:")
    print(list(gen_fibonacci(100)))

    print("8. Filter even numbers:", list(gen_even_filter([10, 15, 22, 33, 40])))

    print("9. Chained generators: numbers → squares")
    numbers = gen_numbers(5)
    squares = gen_squares_from_gen(numbers)
    print(list(squares))

    print("10. Reverse string:")
    print("".join(reverse_string_gen("Generators")))
