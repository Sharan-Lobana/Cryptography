import random

#Convert string initialization vector to stream of bits
#Each character represented by 8 bits
def generate_IV(initialization_vector):
	x = [ord(i) for i in initialization_vector]
	return ''.join('{0:08b}'.format(i) for i in x)

#Generate a key of random ordering of 8 bit numbers
def generate_key(blocksize=8):
	return ['{0:08b}'.format(x) for x in random.sample(range(0,256),256)]

#Return the mapping of first 8 bits of initialization_vector
def blockcipher(initialization_vector,key):
	return key[int(initialization_vector[0:8],base=2)]

#Generate the cipher based on message(string) 
#initialization_vector(bit stream)
#and key(list of 8bit numbers represented as strings of bits) 
def encipher(message,initialization_vector,key):
	length = len(message)
	index = 0
	cipher =''
	IV_encrypted  = blockcipher(initialization_vector,key)
	current_cipher = '{0:08b}'.format(int(IV_encrypted,base=2)^ord(message[index]))
	index += 1
	cipher += current_cipher
	while index != length:
		initialization_vector = initialization_vector[8:]
		initialization_vector += current_cipher
		IV_encrypted = blockcipher(initialization_vector,key)
		current_cipher = '{0:08b}'.format(int(IV_encrypted,base=2)^ord(message[index]))
		cipher += current_cipher
		index +=1
	return cipher 

def decipher(cipher,initialization_vector,key):
	length = len(cipher)/8
	index = 0;
	plaintext = ''
	IV_encrypted = blockcipher(initialization_vector,key)
	current_cipher = cipher[8*index:8*(index+1)]
	plaintext += chr(int(IV_encrypted,base=2)^int(current_cipher,base=2))
	index += 1
	while index != length:
		initialization_vector = initialization_vector[8:]
		initialization_vector += current_cipher
		IV_encrypted = blockcipher(initialization_vector,key)
		current_cipher = cipher[8*index:8*(index+1)]
		index += 1
		plaintext += chr(int(current_cipher,base=2)^int(IV_encrypted,base=2))
	return plaintext
