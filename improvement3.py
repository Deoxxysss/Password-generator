#using functions for future changes
#done some changes to make the output better

import random
import string
import pyperclip

# Character sets
DIGITS = string.digits
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
SYMBOLS = string.punctuation
ALL_CHARACTERS = string.ascii_letters + string.digits + string.punctuation


def generate_password(length):
    """Generate a password containing at least one digit,
    one lowercase letter, one uppercase letter, and one symbol."""

    password = [
        random.choice(DIGITS),
        random.choice(LOWERCASE),
        random.choice(UPPERCASE),
        random.choice(SYMBOLS),
    ]

    password.extend(
        random.choice(ALL_CHARACTERS)
        for _ in range(length - 4)
    )

    random.shuffle(password)
    return "".join(password)


# Number of passwords
while True:
    try:
        count = int(input("Enter the number of passwords you want (1-10): "))
        if 1 <= count <= 10:
            break
        print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Please enter a valid integer.")

# Password length
while True:
    try:
        length = int(input("Enter password length (8-24): "))
        if 8 <= length <= 24:
            break
        print("Password length must be between 8 and 24.")
    except ValueError:
        print("Please enter a valid integer.")

# Generate passwords
passwords = [generate_password(length) for _ in range(count)]

print("\nGenerated Passwords:\n")

for i, password in enumerate(passwords, start=1):
    print(f"{i}. {password}")

# Copy to clipboard
copy_choice = input("\nDo you want to copy the password(s)? (Y/N): ").strip().upper()

if copy_choice == "Y":
    pyperclip.copy("\n".join(passwords))
    print("✅ Password(s) copied to clipboard!")
else:
    print("Passwords were not copied.")