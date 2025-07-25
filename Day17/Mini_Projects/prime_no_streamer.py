def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def prime_streamer(limit):
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        if num == 2:
            num = 3
        else:
            num += 2  # Skip even numbers

    return  # Ends generator naturally

#  usage
if __name__ == "__main__":
    N = 50
    print(f" Prime numbers up to {N}:")
    for prime in prime_streamer(N):
        print(prime, end=" ")
