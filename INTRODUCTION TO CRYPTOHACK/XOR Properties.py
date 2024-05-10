#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
s_2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
s_3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
s_4 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = bytes(a ^ b for (a, b) in zip(key1, s_2))
key3 = bytes(a ^ b for (a, b) in zip(key2, s_3))
flag = bytes(a ^ b ^ c ^ d for (a, b, c, d) in zip(key1, key3, key2, s_4))

print("Here is your flag:")
print("".join(chr(o) for o in flag))

