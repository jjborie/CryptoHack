#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

label = "label"
result = ""
for o in label:
    result += chr(ord(o)^13) 
print("Here is your flag:")
print("crypto{"+result+"}")

