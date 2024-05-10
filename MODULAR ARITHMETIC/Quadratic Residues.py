#!/usr/bin/env python3

def is_quadratic_residue(a, p):
  """Returns True if a is a quadratic residue modulo p, False otherwise."""
  if a < 0:
    return False
  if a == 0:
    return True
  if p == 2:
    return a % 4 == 1
  return pow(a, (p - 1) // 2, p) == 1

p = 29
ints = [14, 6, 11]
for a in ints:
    print(is_quadratic_residue(a,p))


from Crypto.Util.number import *
zn_ = [i for i in range(1,29) if GCD(29,i) == 1]
ints = [14,6,11]
for i in (zn_):
  for j in ints:
    for k in range(1,100):
      if (pow(i, 2) - j == k*29):
        print(i)

p = 29
ints = [14, 6, 11]

qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")