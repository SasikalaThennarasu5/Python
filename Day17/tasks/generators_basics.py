# 1. Generator yielding numbers from 1 to 10
def gen_1_to_10():
    for i in range(1, 11):
        yield i

# 2. Generator yielding even numbers from 1 to n
def gen_even_upto_n(n):
    for i in range(2, n + 1, 2):
        yield i

# 3. Generator yielding squares of numbers from 1 to n
def gen_squares(n):
    for i in range(1, n + 1):
        yield i * i

# 4. Generator yielding characters from a string
def gen_chars(s):
    for ch in s:
        yield ch

# 5. Generator yielding vowels from a string
def gen_vowels(s):
    vowels = 'aeiouAEIOU'
    for ch in s:
        if ch in vowels:
            yield ch

# 6. Manual iteration using next()
def gen_alphabet_5():
    for ch in 'ABCDE':
        yield ch

# 7. Generator that raises StopIteration
def gen_stop_after_3():
    for i in range(3):
        yield i

# 8. Generator yielding prime numbers up to 100
def gen_primes_upto_100():
    for num in range(2, 101):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

# 9. List vs Generator for memory usage
def return_list(n):
    return [i for i in range(n)]

def return_generator(n):
    for i in range(n):
        yield i

# 10. Generator yielding only positive numbers from a list
def gen_positive(nums):
    for num in nums:
        if num > 0:
            yield num

# ----------------- RUN Tasks -----------------
if __name__ == "__main__":
    print("1. Numbers 1 to 10:", list(gen_1_to_10()))
    print("2. Even numbers up to 20:", list(gen_even_upto_n(20)))
    print("3. Squares up to 5:", list(gen_squares(5)))
    print("4. Characters in 'Hello':", list(gen_chars("Hello")))
    print("5. Vowels in 'Beautiful Day':", list(gen_vowels("Beautiful Day")))

    print("6. First 5 letters (manual next):")
    g = gen_alphabet_5()
    try:
        while True:
            print(next(g), end=' ')
    except StopIteration:
        print("\nFinished")

    print("7. StopIteration Demo:")
    g2 = gen_stop_after_3()
    try:
        while True:
            print(next(g2), end=' ')
    except StopIteration:
        print("\nStopIteration raised!")

    print("8. Prime numbers up to 100:")
    print(list(gen_primes_upto_100()))

    print("9. Memory usage comparison (using sys.getsizeof):")
    import sys
    lst = return_list(100000)
    gen = return_generator(100000)
    print("List memory (100000):", sys.getsizeof(lst))
    print("Generator memory (100000):", sys.getsizeof(gen))

    print("10. Positive numbers from list:")
    sample_list = [-3, 5, 0, -1, 8, 12]
    print(list(gen_positive(sample_list)))
