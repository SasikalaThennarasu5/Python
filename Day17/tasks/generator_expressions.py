# 1. Generator expression to yield squares of numbers from 1 to 10
squares_gen = (x * x for x in range(1, 11))

# 2. Generator expression to yield all odd numbers in a list
nums = [1, 4, 7, 10, 13, 16]
odd_gen = (x for x in nums if x % 2 != 0)

# 3. Convert generator expression to a list using list()
gen_list = list(x * 2 for x in range(5))

# 4. Generator expression for words longer than 5 characters
sentence = "Generator expressions are memory efficient and powerful"
long_words_gen = (word for word in sentence.split() if len(word) > 5)

# 5. Generator expression for uppercase letters in a string
text = "Python3.10 Rocks!"
uppercase_letters = (ch for ch in text if ch.isupper())

# 6. Compare generator vs list comprehension memory usage
import sys
gen_large = (x for x in range(1000000))
list_large = [x for x in range(1000000)]

# 7. Generator expression with sum() to calculate total
total_sum = sum(x for x in range(1, 101))

# 8. Generator expression to filter floats from a mixed list
mixed_list = [1, 2.5, "hello", 3.14, True, 7.0, None]
float_gen = (x for x in mixed_list if isinstance(x, float))

# 9. Use generator expression with any() to check divisibility by 3
numbers = [4, 7, 9, 11]
has_divisible_by_3 = any(x % 3 == 0 for x in numbers)

# 10. Use generator expression with max() to get highest number
values = [5, 12, 8, 99, 34]
max_value = max(x for x in values)

# ---------------------- RUN EXAMPLES ----------------------
if __name__ == "__main__":
    print("1. Squares from 1 to 10:", list(squares_gen))

    print("2. Odd numbers from list:", list(odd_gen))

    print("3. Generator to list (double):", gen_list)

    print("4. Words longer than 5 characters:", list(long_words_gen))

    print("5. Uppercase letters:", list(uppercase_letters))

    print("6. Memory usage:")
    print("  List comprehension (1000000):", sys.getsizeof(list_large), "bytes")
    print("  Generator expression (1000000):", sys.getsizeof(gen_large), "bytes")

    print("7. Sum of numbers 1 to 100:", total_sum)

    print("8. Filtered floats:", list(float_gen))

    print("9. Any number divisible by 3:", has_divisible_by_3)

    print("10. Max value in list:", max_value)
