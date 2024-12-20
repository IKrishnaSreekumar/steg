import random

# Function to compute the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular inverse
def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    old_r, r = e, phi
    old_s, s = 1, 0
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    if old_r != 1:  # No modular inverse if GCD(e, phi) != 1
        raise ValueError("e and phi are not coprime")
    return old_s % phi

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a random prime number
def generate_prime(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# RSA key generation
def generate_rsa_keys():
    # Step 1: Generate two large prime numbers, p and q
    p = generate_prime(1000, 5000)
    q = generate_prime(1000, 5000)
    
    # Step 2: Compute n = p * q
    n = p * q
    
    # Step 3: Compute phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)
    
    # Step 4: Choose an encryption key e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    # Step 5: Compute the decryption key d such that (e * d) % phi(n) = 1
    d = mod_inverse(e, phi)
    
    # Public key: (e, n), Private key: (d, n)
    return (e, n), (d, n)

# Generate keys
public_key, private_key = generate_rsa_keys()

print("Public Key (e, n):", public_key)
print("Private Key (d, n):",private_key)

# Save keys to a file
with open("public_key.py", "w") as f:
    f.write(f"public_key = {public_key}\n")
    

with open("private_key.py", "w") as f:
    f.write(f"private_key = {private_key}\n")