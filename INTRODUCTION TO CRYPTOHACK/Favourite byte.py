#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


print("Test flags:")

keys = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for k in range(0,256):
    decrypt_key = bytes(a ^ k for (a) in keys)
    flag = "".join(chr(o) for o in decrypt_key)
    #print(flag + " : " + k)
    if flag.startswith("crypto"):
        print(flag)


