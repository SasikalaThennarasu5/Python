from cryptography.fernet import Fernet

def log_encryptions(func):
    def wrapper(*args, **kwargs):
        print(f"Encrypting: {args[1]}")
        return func(*args, **kwargs)
    return wrapper

class Cipher:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    @log_encryptions
    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
            encrypted = self.cipher.encrypt(data)
            with open(file_path + '.enc', 'wb') as file:
                file.write(encrypted)
        except Exception as e:
            print(f"Encryption failed: {e}")

    def decrypt_file(self, enc_path, output_path):
        try:
            with open(enc_path, 'rb') as file:
                data = file.read()
            decrypted = self.cipher.decrypt(data)
            with open(output_path, 'wb') as file:
                file.write(decrypted)
        except Exception as e:
            print(f"Decryption failed: {e}")

if __name__ == "__main__":
    cipher = Cipher()
    print("Key:", cipher.key.decode())
    mode = input("Encrypt or Decrypt (e/d)? ").lower()
    if mode == 'e':
        path = input("Enter file path to encrypt: ")
        cipher.encrypt_file(path)
    elif mode == 'd':
        path = input("Enter encrypted file path: ")
        out = input("Enter output file path: ")
        cipher.decrypt_file(path, out)
    else:
        print("Invalid option.")
