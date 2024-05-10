#!/usr/bin/env python3

def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)

a = 66528
b = 52920
 
print("The gcd of {a} and {b} is : ", end="")
print(hcfnaive(a, b))