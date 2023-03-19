import string
import secrets

def generate_secure_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_numbers else ""
    special_chars = string.punctuation if include_special_chars else ""

    # Combine character sets and create a password
    all_characters = lowercase_letters + uppercase_letters + digits + special_chars
    if len(all_characters) == 0:
        raise ValueError("At least one character set must be included")

    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Customize password requirements here
    password_length = 16
    include_uppercase = True
    include_numbers = True
    include_special_chars = True

    # Generate and print a secure password
    generated_password = generate_secure_password(password_length, include_uppercase, include_numbers, include_special_chars)
    print("Generated secure password:", generated_password)
