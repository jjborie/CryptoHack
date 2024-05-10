#!/usr/bin/env python3

from mod import Mod

# My RSA keys
public_key = Mod(3, 61423)
private_key = Mod(40619, 61423)

# My very secret message
top_secret_message = 666
print(top_secret_message)

# RSA encryption
encrypted = top_secret_message**public_key
print(encrypted)

# RSA decryption
decrypted = encrypted**private_key
print(decrypted)

# My secret message have been correctly encrypted and decrypted :-)
assert decrypted == top_secret_message