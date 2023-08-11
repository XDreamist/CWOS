import os
from Crypto.Cipher import AES

aes_key = os.urandom(32)  # Generate a 32-byte AES key (AES-256)
iv = os.urandom(16)      # Generate a 16-byte IV

aes_key_hex = aes_key.hex()
iv_hex = iv.hex()

print("Generated AES Key:", aes_key_hex)
print("Generated IV:", iv_hex)


