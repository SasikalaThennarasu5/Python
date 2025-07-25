# Basic Iterator and Iterable Understanding

# 1. Use iter() and next() to iterate over a list manually.
print("1. Manual iteration over list:")
my_list = [10, 20, 30]
it = iter(my_list)
print(next(it))
print(next(it))
print(next(it))

# 2. Use a for loop vs while with next() to iterate a tuple.
print("\n2. For loop vs while loop (tuple):")
my_tuple = (1, 2, 3)
print("Using for loop:")
for item in my_tuple:
    print(item)

print("Using while loop and next():")
tuple_iter = iter(my_tuple)
while True:
    try:
        print(next(tuple_iter))
    except StopIteration:
        break

# 3. Check if a variable is iterable using dir()
print("\n3. Check if variable is iterable using dir():")
var = [1, 2, 3]
if "__iter__" in dir(var):
    print("Yes, it's iterable.")
else:
    print("No, it's not iterable.")

# 4. Try to use next() on a non-iterator and handle exception
print("\n4. Using next() on non-iterator:")
non_iter = 100
try:
    print(next(non_iter))  # Not an iterator
except TypeError as e:
    print("TypeError:", e)

# 5. Consume only first 3 elements of a set using next()
print("\n5. First 3 elements of a set:")
my_set = {"a", "b", "c", "d"}
set_iter = iter(my_set)
for _ in range(3):
    print(next(set_iter))

# 6. Use next() to iterate through characters in a string.
print("\n6. next() on string characters:")
my_string = "Hello"
string_iter = iter(my_string)
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))

# 7. Use iter() on dictionary and fetch only keys
print("\n7. Iterate dictionary keys:")
my_dict = {"name": "Alice", "age": 25}
dict_iter = iter(my_dict)
for key in dict_iter:
    print(key)

# 8. Convert range to iterator and loop with next()
print("\n8. range() with next():")
r = range(5)
r_iter = iter(r)
while True:
    try:
        print(next(r_iter))
    except StopIteration:
        break

# 9. Function that takes iterable and prints using next()
print("\n9. Function to consume iterable with next():")
def consume_iterable(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

consume_iterable(["apple", "banana", "cherry"])

# 10. Handle StopIteration after consuming all items
print("\n10. Handling StopIteration:")
lst = [1, 2]
lst_iter = iter(lst)
try:
    print(next(lst_iter))
    print(next(lst_iter))
    print(next(lst_iter))  # One extra
except StopIteration:
    print("Reached end of iterator. StopIteration handled.")
