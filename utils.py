''' Contains utility functions for 
encryption and decryption
Author: Sharan Lobana
Created: 2016-01-07
'''
import random
import numpy as np 
import string
#GCD using Euclid's algorithm
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

#Iterative implementation of gcd using Euclid's algorithm
def iterative_gcd(a,b):
	while b:
		a,b = b,a%b
	return a 

#GCD using bit operations
def bgcd(a,b):
	if a == b: return a
	if a == 0: return b 
	if b == 0: return a
	if (~a & 1): #if a is even
		if(~b & 1): # if b is even
			return bgcd(a>>1,b>>1)<<1  #gcd(a,b) = 2*gcd(a/2,b/2)
		else:
			return bgcd(a>>1,b)   #gcd(a,b) = gcd(a/2,b)
	else:	#if a is odd
		if(~b & 1):	#if b is even
			return bgcd(a,b>>1)	#gcd(a,b) = gcd(a,b/2)
		else:	#if b is odd
			if (a>b):
				return bgcd((a-b)>>1,b)	#from the Euler's algorithm
	#if a and b both are odd and b<a
	return bgcd((b-a)>>1,a)	#b-a is even and gcd(b-a,b)= gcd((b-a)/2,b)

def modular_multiplicative_inverse(a,n):
	t = 0
	nt = 1
	r = n
	nr = a%n 
	if n < 0:
		n = -n
	if a < 0:
		a = n - (-a%n)
	while nr != 0:
		quot = (r/nr) | 0
		tmp = nt 
		nt = t - quot*nt 
		t = tmp
		tmp = nr 
		nr = r - quot*nr 
		r = tmp
	if r > 1:
		return -1
	if t < 0:
		t += n
	return t 

#character to integer mapping A-Z to 0-25
def char_to_int(char):
	return ord(char) - 65

#integer to character mapping 0-25 to A-Z
def int_to_char(integer):
	return chr(integer + 65)

#Utility function to generate random string of specified length
def generate_random_string(length):
	return ''.join(random.choice(string.ascii_lowercase)\
	 for _ in range(length))

#key generation for Hill cipher
def generate_key_hill():
		key = [[0 for x in range(3)] for x in range(3)]
		for i in range(3):
			for j in range(3):
				#Fill the key with random numbers in the range 0-25
				key[i][j] = int(random.random()*26) 

		#declare a numpy matrix
		key_matrix = np.matrix(key)

		#Genrate a new key if the key_matrix is non-invertible i.e det=0
		if round(np.linalg.det(key_matrix)) == 0:
			return generate_key_hill()

		#Generate a key if modular inverse of det w.r.t (mod 26) doesn't exist
		#i.e if the gcd of determinant and 16 is not equal to 1
		elif gcd(round(np.linalg.det(key_matrix))%26,26) != 1:
			return generate_key_hill()

		return key_matrix
#key generation for transposition cipher
def generate_key_transposition():
	return random.sample(range(0,5),5)

#Key alignment and plaintext filtering for Vignere Cipher
def alignment(cipher,key):
		l1 = len(key)
		l2 = len(cipher)
		cipher = cipher.upper()
		key = key.upper()
		aligned_key = ''
		if l1 >= l2:
			aligned_key = key[:l2]
		else:
			repeatitions = l2/l1
		for i in range(repeatitions):
			aligned_key += key
		if (l2%l1) !=0:
			aligned_key +=key[:l2%l1]
		return (cipher,aligned_key)