# Password Generator

import random
import string
import json
from getpass import getpass

class PasswordGenerator:
    def __init__(self):
        self.saved_passwords = []
        self.encrypted_file = "passwords.json"

    def generate(self, length=12, use_upper=True, use_digits=True, use_symbols=True):
        chars = string.ascii_lowercase
        if use_upper:
            chars += string.ascii_uppercase
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        if not chars:
            raise ValueError("No characters available to generate password.")
        
        password = ''.join(random.choice(chars) for _ in range(length))
        strength = self.strength_meter(password)
        return password, strength

    def strength_meter(self, password):
        length = len(password)
        score = 0
        if any(c.islower() for c in password): score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        if length >= 12: score += 1

        return ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"][score - 1]

    def save_passwords(self, master_key):
        encrypted = []
        for pw in self.saved_passwords:
            encrypted.append("".join(chr(ord(c) ^ ord(master_key[i % len(master_key)])) for i, c in enumerate(pw)))
        with open(self.encrypted_file, 'w') as f:
            json.dump(encrypted, f)

    def load_passwords(self, master_key):
        try:
            with open(self.encrypted_file, 'r') as f:
                encrypted = json.load(f)
                self.saved_passwords = ["".join(chr(ord(c) ^ ord(master_key[i % len(master_key)])) for i, c in enumerate(enc)) for enc in encrypted]
        except FileNotFoundError:
            self.saved_passwords = []

# CLI for demo
if __name__ == "__main__":
    gen = PasswordGenerator()
    master_key = getpass("Enter master key for encryption: ")
    gen.load_passwords(master_key)

    while True:
        print("\n--- Password Generator ---")
        print("1. Generate Password\n2. View Saved Passwords\n3. Save & Exit")
        choice = input("Choose: ")

        if choice == '1':
            length = int(input("Length: "))
            use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            pw, strength = gen.generate(length, use_upper, use_digits, use_symbols)
            print(f"Generated: {pw}\nStrength: {strength}")
            save = input("Save this password? (y/n): ").lower() == 'y'
            if save:
                gen.saved_passwords.append(pw)
        elif choice == '2':
            print("\nSaved Passwords:")
            for i, pw in enumerate(gen.saved_passwords, 1):
                print(f"{i}. {pw}")
        elif choice == '3':
            gen.save_passwords(master_key)
            print("Passwords saved and encrypted. Exiting.")
            break
