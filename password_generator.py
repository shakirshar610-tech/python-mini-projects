import secrets
import string

length = int(input("Password length: "))

if length < 8:
    raise ValueError("Use at least 8 characters.")

alphabet = string.ascii_letters + string.digits + string.punctuation
password = "".join(secrets.choice(alphabet) for _ in range(length))

print("Generated password:", password)
