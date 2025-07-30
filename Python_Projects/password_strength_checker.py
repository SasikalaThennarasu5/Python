
import re

def evaluate_strength(password):
    if not password:
        raise ValueError("Password cannot be empty.")

    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add a special character.")

    if strength <= 2:
        return "Weak", feedback
    elif strength == 3 or strength == 4:
        return "Medium", feedback
    else:
        return "Strong", feedback


def generator_missing_criteria(password):
    _, feedback = evaluate_strength(password)
    for message in feedback:
        yield message


def main():
    while True:
        pwd = input("Enter a password to evaluate (or 'exit' to quit): ")
        if pwd.lower() == "exit":
            break

        try:
            strength, _ = evaluate_strength(pwd)
            print(f"Password Strength: {strength}")

            if strength != "Strong":
                print("Suggestions:")
                for suggestion in generator_missing_criteria(pwd):
                    print(f"- {suggestion}")
        except ValueError as ve:
            print(ve)


if __name__ == "__main__":
    main()
