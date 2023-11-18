import random
import string


def generate_password(length=10, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("You must select at least one character type.")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")

    use_letters = input("Include letters (y/n): ").lower() == "y"
    use_numbers = input("Include numbers (y/n): ").lower() == "y"
    use_symbols = input("Include symbols (y/n): ").lower() == "y"

    length = int(input("Enter the password length (8-12): "))
    if length < 8 or length > 12:
        print("Invalid password length. It must be between 8 and 12 characters.")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Generated Password:", password)


if __name__ == "__main__":
    main()