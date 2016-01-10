#Python implementation of Counter Mode Cipher
#A user supplied string key is converted into a 8 bit number 
#Each PlainText byte is XORed with the 8 bit number 
#which is incremented in a modulo 2**8 way after XORing operation
import SHA_1 as s 

def generate_key_counter(string):
	return s.sha1(string,True)[0][:8]

def encipher(plaintext,key):
	return encipher_decipher(''.join('{0:08b}'.format(ord(x)) for x in plaintext),key)

def decipher(cipher,key):
	deciphered_bit_stream = encipher_decipher(cipher,key)
	decipher = ''
	for i in range(len(deciphered_bit_stream)/8):
		decipher += chr(int(deciphered_bit_stream[8*i:8*(i+1)],base=2))
	return decipher 

def encipher_decipher(binary_plaintext,key):
	length = len(binary_plaintext)/8
	key = int(key,base=2)
	cipher = ''
	for i in range(length):
		cipher += '{0:08b}'.format(int(binary_plaintext[8*i:8*(i+1)],base=2)^key)
		key += 1
		key%=256
	return cipher 