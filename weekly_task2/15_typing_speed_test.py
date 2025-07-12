import time
sample = "Python is a powerful programming language."

input("Press Enter to start typing test...")
print("Type this:")
print(sample)
start = time.time()
typed = input("\nStart typing: ")
end = time.time()

time_taken = end - start
words = len(typed.split())
speed = words / (time_taken / 60)
errors = sum(1 for a, b in zip(sample, typed) if a != b)

print(f"\nTime: {time_taken:.2f} sec\nSpeed: {speed:.2f} WPM\nErrors: {errors}")
