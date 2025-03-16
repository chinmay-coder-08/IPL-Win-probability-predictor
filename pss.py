import random

# Generate a random key (same length as the text)
def generate_key(length):
    random.seed(42)  # Ensure repeatability (change this for security)
    return [random.randint(1, 255) for _ in range(length)]

# Encrypt function
def custom_encrypt(text, key):
    encrypted_chars = [(ord(char) + key[i]) % 256 for i, char in enumerate(text)]
    return ''.join(chr(c) for c in encrypted_chars)

# Decrypt function
def custom_decrypt(encrypted_text, key):
    decrypted_chars = [(ord(char) - key[i]) % 256 for i, char in enumerate(encrypted_text)]
    return ''.join(chr(c) for c in decrypted_chars)

# Example Usage
plaintext = "chinmyfgbyfgr"
key = generate_key(len(plaintext))  # Generate a key

encrypted_text = custom_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = custom_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
