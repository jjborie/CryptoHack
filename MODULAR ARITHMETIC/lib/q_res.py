#! /usr/bin/env python
#
# https://asecuritysite.com/encryption/q_res?Length=10
import sys
import random
import libnum


p=11
q=13




y=25

if (len(sys.argv)>1):
        y=int(sys.argv[1])
if (len(sys.argv)>2):
        p=int(sys.argv[2])
if (len(sys.argv)>3):
        q=int(sys.argv[3])

N=p*q



print ("p=",p)
print ("q=",q)
print ("y=",y)

print ("\n\nFind solution to x^2 = y (mod N)")
# Find solution to x^2 = y (mod N)

if (libnum.has_sqrtmod(y,{p: 1,q:1})):
	x=next(libnum.sqrtmod(y,{p: 1,q:1}))
	print (int(x))
	
	print ("x=",x)
	print ("N=",N)
	print ("  %d^2=%d (mod %d)" % (x,y,N))
else:
	print ("No Solution!!!!")


print ("\n\nFind solution to x^2 = y (mod p)")
# Find solution to x^2 = y (mod p)

if (libnum.has_sqrtmod(y,{p: 1})):
	x=next(libnum.sqrtmod(y,{p: 1}))

	
	print ("x=",x)
	print ("p=",p)
	print ("  %d^2=%d (mod %d)" %(x,y,p))
else:
	print ("No Solution!!!!")


print ("\n\nFind solution to x^2 = y (mod q)")
# Find solution to x^2 = y (mod q)

if (libnum.has_sqrtmod(y,{q: 1})):
	x=next(libnum.sqrtmod(y,{q: 1}))

	
	print ("x=",x)
	print ("q=",q)
	print ("  %d^2=%d (mod %d)" %(x,y,q))
else:
	print (")No Solution!!!!")