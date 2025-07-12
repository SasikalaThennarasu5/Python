def star_pattern(n):
    for i in range(1, n+1):
        print('*' * i)

def triangle_pattern(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))

def number_pattern(n):
    for i in range(1, n+1):
        print(' '.join(str(j) for j in range(1, i+1)))

while True:
    print("\n1. Star\n2. Triangle\n3. Numbers\n4. Exit")
    ch = input("Pattern type: ")
    if ch == '4': break
    try:
        size = int(input("Size: "))
    except:
        print("Invalid size")
        continue
    if ch == '1': star_pattern(size)
    elif ch == '2': triangle_pattern(size)
    elif ch == '3': number_pattern(size)
    else: print("Invalid choice")