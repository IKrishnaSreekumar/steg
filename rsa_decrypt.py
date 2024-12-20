# rsa_decrypt.py
from private_key import private_key

# Function to decrypt a message using RSA
def rsa_decrypt(encrypted_message, key):
    d, n = key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Get the encrypted message from user input
encrypted_message = input("Enter the encrypted message (as a list of numbers): ")

# Convert the input string into a list of integers
encrypted_message = list(map(int, encrypted_message.strip("[]").split(", ")))

# Decrypt the message
decrypted_message = rsa_decrypt(encrypted_message, private_key)

print("Decrypted message:", decrypted_message)
