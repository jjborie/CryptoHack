<script>gtag('event', 'Downloaded Script', {
      'event_category' : 'Coding',
      'event_label' : 'Python'
       });</script>'''
Source: extendedeuclideanalgorithm.com
'''

import math 

#Warning: can't handle b=0. See extendedeuclideanalgorithm.com/code for a version that can
def gcd_iterative(a, b):
	""" Calculating the greatest common divisor 
	using the Euclidean Algorithm (non-recursive) 
	(Source: extendedeuclideanalgorithm.com/code) 
	"""
  
	#Set default values for the quotient and the remainder
	q = 0
	r = 1
	
	'''
	In each iteration of the loop below, we
	calculate the new quotient, remainder, a and b.
	r decreases, so we stop when r = 0 
	'''
	while(r > 0):
		#The calculations
		q = math.floor(a/b)
		r = a - q * b
		
		#The values for the next iteration
		a = b
		b = r if (r > 0) else b
	
	return abs(b)


#Can handle b=0
def gcd_iterative_2(a, b):
   """ Calculating the greatest common divisor 
   using the Euclidean Algorithm (non-recursive) 
   (Source: extendedeuclideanalgorithm.com/code) 
   """
  
   #Set default values for the quotient and the remainder
   q = 0
   r = 1
   
   '''
   In each iteration of the loop below, we
   calculate the new quotient, remainder, a and b.
   r decreases, so we stop when r = 0 
   '''
   while(b > 0):
      #The calculations
      q = math.floor(a/b)
      r = a - q * b
      
      #The values for the next iteration
      a = b
      b = r
   
   return abs(a)


def gcd(a, b):
   """ Calculating the greatest common divisor 
   using the Euclidean Algorithm (recursive) 
   (Source: extendedeuclideanalgorithm.com/code)
   """
   if(b == 0):
      return abs(a)
   
   q = math.floor(a/b)
   r = a - q * b
   return abs(b) if (r == 0) else gcd(b, r)
   
   

#Warning: this version can't handle b=0. See extendedeuclideanalgorithm.com/code for a version that can.
def xgcd_iterative(a, b):
	""" Calculates the gcd and Bezout coefficients, 
	using the Extended Euclidean Algorithm (non-recursive).
	(Source: extendedeuclideanalgorithm.com/code) 
	"""
	#Set default values for the quotient, remainder, 
	#s-variables and t-variables
	q = 0
	r = 1
	s1 = 1 
	s2 = 0
	s3 = 1 
	t1 = 0 
	t2 = 1
	t3 = 0
	
	'''
	In each iteration of the loop below, we
	calculate the new quotient, remainder, a, b,
	and the new s-variables and t-variables.
	r decreases, so we stop when r = 0
	'''
	while(r > 0):
		#The calculations
		q = math.floor(a/b)
		r = a - q * b
		s3 = s1 - q * s2
		t3 = t1 - q * t2
		
		'''
		The values for the next iteration, 
		(but only if there is a next iteration)
		'''
		if(r > 0):
			a = b
			b = r
			s1 = s2
			s2 = s3
			t1 = t2
			t2 = t3

	return abs(b), s2, t2

#Can handle b=0
def xgcd_iterative_2(a, b):
   """ Calculates the gcd and Bezout coefficients, 
   using the Extended Euclidean Algorithm (non-recursive).
   (Source: extendedeuclideanalgorithm.com/code) 
   """
   #Set default values for the quotient, remainder, 
   #s-variables and t-variables
   q = 0
   r = 1
   s1 = 1 
   s2 = 0
   s3 = 1 
   t1 = 0 
   t2 = 1
   t3 = 0
   
   '''
   In each iteration of the loop below, we
   calculate the new quotient, remainder, a, b,
   and the new s-variables and t-variables.
   r decreases, so we stop when r = 0
   '''
   while(b > 0):
      #The calculations
      q = math.floor(a/b)
      r = a - q * b
      s3 = s1 - q * s2
      t3 = t1 - q * t2
      
      '''
      The values for the next iteration, 
      (but only if there is a next iteration)
      '''
     
      a = b
      b = r
      s1 = s2
      s2 = s3
      t1 = t2
      t2 = t3

   return abs(a), s1, t1


def xgcd(a, b, s1 = 1, s2 = 0, t1 = 0, t2 = 1):
   """ Calculates the gcd and Bezout coefficients, 
   using the Extended Euclidean Algorithm (recursive).
   (Source: extendedeuclideanalgorithm.com/code) 
   """
   if(b == 0):
      return abs(a), 1, 0
   
   q = math.floor(a/b)
   r = a - q * b
   s3 = s1 - q * s2
   t3 = t1 - q * t2
   
   #if r==0, then b will be the gcd and s2, t2 the Bezout coefficients
   return (abs(b), s2, t2) if (r == 0) else xgcd(b, r, s2, s3, t2, t3)



def multinv(b, n):
   """
   Calculates the multiplicative inverse of a number b mod n,
   using the Extended Euclidean Algorithm. If b does not have a
   multiplicative inverse mod n, then throw an exception.
   (Source: extendedeuclideanalgorithm.com/code)
   """
   
   #Get the gcd and the second Bezout coefficient (t)
   #from the Extended Euclidean Algorithm. (We don't need s)
   my_gcd, _, t = xgcd(n, b)
   
   #It only has a multiplicative inverse if the gcd is 1
   if(my_gcd == 1):
      return t % n
   else:
      raise ValueError('{} has no multiplicative inverse modulo {}'.format(b, n))


def main():
   #Use your own values for a and b
   a = 34
   b = 24
   
   '''
   Euclidean algorithm: 
   see the output of gcd(a, b)
   '''
   print('Euclidean Algorithm:')
   print('The gcd of', a, 'and', b, 'is', gcd(a, b))
   
   #-------------------------------------------------------------
   
   '''
   Extended Euclidean Algorithm:
   see the output of xgcd(a,b) and Bezout coefficients
   And verify that they are correct
   '''
   my_gcd, s, t = xgcd(a, b)
   verification = abs(s*a+t*b)
   print('Extended Euclidean Algorithm:')
   print('The gcd of', a, 'and', b, 'is', my_gcd)
   print('And the Bezout coefficients: s=', s, ' and t=', t, '.', sep='')
   print('And', s, '*', a, '+', t, '*', b, '=', verification)
   if(my_gcd == verification):
         print('So as we expect, s*a+t*b is equal to the gcd we found.') 
   else:
         print('Something went wrong')
   
  #------------------------------------------------------------      
   b = 10
   n = 15
  
   '''
   Multiplicative Inverse:
   Try to compute the multiplicative inverse of b mod n.
   If that succeeds, verify that it's correct.
   If it doesn't succeed, show the error raised by the function.
   '''
 
   print('Multiplicative inverse:')
   try:
      inverse = multinv(b, n);
      print('We discovered that the multiplicative inverse of',
      b, 'mod', n, 'equals', inverse)
      verification = (inverse * b % n == 1)
      if(verification):
            print('And indeed,', b, '*', inverse, 'mod', n, '= 1')
      else:
            print('This is not correct.')    
   except ValueError as error:
      print(error)


#Use main() as main function when you run this script
if __name__== "__main__":
  main()