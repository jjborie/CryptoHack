#!/usr/bin/env python3

import sys
from Crypto.Util import *
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

def repeat_str(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]
secret = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
secret_hex = bytes.fromhex(secret)

start_secret = 'crypto{'

key = bytes(ord(a) ^ b for (a, b) in zip(start_secret, secret_hex[:7]))
print("partial key: {}".format(key))

complete_key = repeat_str(key, len(secret))
print('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(complete_key)

flag = bytes(a ^ ord(b) for (a, b) in zip(complete_key, secret))
print("".join(chr(o) for o in flag))
