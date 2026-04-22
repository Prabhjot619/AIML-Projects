# Smart Password Strength Analyzer + Generator

import random
import string

def check_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong 💪"

    return strength, suggestions

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    while True:
        print("\n--- Password Tool ---")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            pwd = input("Enter password: ")
            strength, suggestions = check_strength(pwd)

            print("\n🔍 Strength:", strength)

            if suggestions:
                print("💡 Suggestions:")
                for s in suggestions:
                    print("-", s)

        elif choice == "2":
            length = int(input("Enter desired length: "))
            print("\n🔐 Generated Password:", generate_password(length))

        elif choice == "3":
            break
        else:
            print("Invalid choice!")

main()