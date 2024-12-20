# rsa_encrypt.py

from public_key import public_key

# Function to encrypt a message using RSA
def rsa_encrypt(message, key):
    e, n = key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Get user input
message = input("Enter the message to encrypt: ")

# Encrypt the message
encrypted_message = rsa_encrypt(message, public_key)

print("Encrypted message:", encrypted_message)
with open("encrypt.py", "w") as f:
    f.write(f"encrypt = {encrypted_message}\n")
