''' Contains utility functions for 
encryption and decryption
Author: Sharan Lobana
Created: 2016-01-07
'''
import random
import numpy as np 
def gcd(b,a):
	if b==0:
		return a
	if a == 0:
		return b
	return gcd(a%b,b)

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