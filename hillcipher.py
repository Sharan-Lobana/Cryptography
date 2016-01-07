#Hill Cipher implementation in python

#The integers 0-25 map to A-Z
#The message to be encrypted can contain characters in a-z,A-Z and whitespace
#The ciphered text is assumed to be in uppercase alphabets

import random
import numpy as np 

#Utility function for character to integer mapping A-Z to 0-25
def char_to_int(char):
	return ord(char) - 65

#Utility function for integer to character mapping 0-25 to A-Z
def int_to_char(integer):
	return chr(integer + 65)

#Utility function for computing the greatest common divisior 
#(highest common factor) using Euclid's formula
def gcd(b,a):
	if b==0:
		return a
	if a == 0:
		return b
	return gcd(a%b,b)

#Utility function to find the modular multiplicative inverse
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

#Function for generating the 3x3 key for encryption
def generate_key():
	key = [[0 for x in range(3)] for x in range(3)]
	for i in range(3):
		for j in range(3):
			#Fill the key with random numbers in the range 0-25
			key[i][j] = int(random.random()*26) 

	#declare a numpy matrix
	key_matrix = np.matrix(key)

	#Genrate a new key if the key_matrix is non-invertible i.e det=0
	if round(np.linalg.det(key_matrix)) == 0:
		return generate_key()

	#Generate a key if modular inverse of det w.r.t (mod 26) doesn't exist
	#i.e if the gcd of determinant and 16 is not equal to 1
	elif gcd(round(np.linalg.det(key_matrix))%26,26) != 1:
		return generate_key()

	return key_matrix

#The append_value specifies the character to be appended to 
#text to make its length a multiple of 3 for complete trigrams 
def encipher(message,key_matrix,append_value='X'):
	message = message.replace(' ','')
	message = message.upper()
	cipher = ''
	length = len(message)
	if any(ord(x)>90 or ord(x)<65 for x in message):
		return "Illegal message"
	
	remaining = -length%3

	for x in range(remaining):
		message = message + append_value
	num_trigrams = len(message)/3	
	for i in range(num_trigrams):
		tri = message[3*i:3*(i+1)]
		p = [char_to_int(x) for x in tri]
		p_vector = np.matrix(p)
		c_vector = (key_matrix*p_vector.T)%26
		for x in c_vector:
			cipher += str(int_to_char(x.item()))
	return cipher 

def decipher(cipher,key_matrix):
	#Convert the cipher to uppercase
	cipher = cipher.upper()
	#Replace any whitespace if present
	cipher = cipher.replace(' ','')
	length = len(cipher)

	#Return illegal if the cipher contains characters other 
	#than A-Z or length of cipher is not a multiple of 3
	if any(ord(x) > 90 or ord(x) < 65 for x in cipher) or length%3 != 0:
		return "Illegal cipher"
	d = round(np.linalg.det(key_matrix))
	#If the key_matrix is non-invertible return 
	if  d == 0:
		return "Invalid key" 
	original_message = ''

	#Compute the inverse of the key array
	matrix_inverse = np.linalg.inv(key_matrix)

	#Compute the adjoint from the inverse
	adjoint = np.rint(matrix_inverse*d).astype(int)

	#Compute the modular multiplicative inverse of determinant
	d_inverse  = modular_multiplicative_inverse(int(d),26)

	#Compute the modular multiplicative inverse for the key_matrix
	inverse = d_inverse*adjoint
	for i in range(length/3):

		#Select a trigram from the cipher
		tri = cipher[3*i:3*(i+1)]
		c = [char_to_int(x) for x in tri] #Convert the chars to integers in 0-25
		c_vector = np.matrix(c) #declare a numpy vector
		p_vector = (inverse*c_vector.T).astype(int)%26 #Decrypt the cipher

		#Perform integer to character mapping
		for x in p_vector:
			original_message += int_to_char(x.item())
	return original_message




