def encode(msg):
    return ' '.join(str(ord(c)) for c in msg)

def decode(code):
    return ''.join(chr(int(num)) for num in code.split())

while True:
    print("\n1. Encode\n2. Decode\n3. Exit")
    ch = input("Choose: ")
    if ch == '1':
        m = input("Enter message: ")
        print("Encoded:", encode(m))
    elif ch == '2':
        c = input("Enter code: ")
        print("Decoded:", decode(c))
    elif ch == '3': break
    else: print("Invalid")