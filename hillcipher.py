'''implements Hill cipher 
Author: Sharan Lobana
Created : 2016-01-07
'''

#The integers 0-25 map to A-Z
#The message to be encrypted can contain characters in a-z,A-Z and whitespace
#The ciphered text is assumed to be in uppercase alphabets


import numpy as np 
from utils import modular_multiplicative_inverse,generate_key_hill,gcd,char_to_int,int_to_char 

class HillCipher():
	'''The Hill cipher encrypts a trigrams of characters,
	the key consists of 3x3 square matrix having numbers 
	in the range 0 to 25 inclusive of both
	More information about the algorithm can be 
	found at http://www.practicalcryptography.com/ciphers/hill-cipher/
	@param key: The keysquare consists pseudorandom numbers ,an integer
	parameter can be given as a seed for the pseudorandom number genreation
	'''
	#Function for generating the 3x3 key for encryption
	def __init__(self):
		self.key = generate_key_hill()
	
	def set_key(self):
		self.key = generate_key_hill()
	#The append_value specifies the character to be appended to 
	#text to make its length a multiple of 3 for complete trigrams 
	def encipher(self,message,key_matrix=None,append_value='X'):
		if key_matrix == None:
			key_matrix = self.key 
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

	def decipher(self,cipher,key_matrix=None):
		if key_matrix == None:
			key_matrix = self.key 
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




