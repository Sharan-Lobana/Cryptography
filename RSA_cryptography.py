#Python implementation of RSA encryption 
import random
from utils import modular_multiplicative_inverse

#Primality Test O(sqrt(n)) time complexity
def isPrime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

#Utility function to generate a random prime in a given range(both inclusive)
def random_prime(mini,maxi):
	p = random.randint(mini,maxi)
	if isPrime(p):
		return p
	else :
		return random_prime(mini,maxi)

#Main function to generate the RSA-keys
def generate():
	p = random_prime(2,255) #8 bit
	q = random_prime(2,255) #8 bit
	n = p*q
	t = (p - 1)*(q - 1) # Totient 
	e = random_prime(2,t)
	d = modular_multiplicative_inverse(e,t)

	return {'public_key':[n,e],'private_key':d}

#Encryption of a number
def encrypt(m,n,e):
	return pow(m,e,n)

#Decryption of a number
def decrypt(mEnc,d,n):
	return pow(mEnc,d,n)

#Encryption of a message 
#Returns a list of the encrypted ciphers
def encrypted_message(message,n,e):
	encrypted_list = []
	for i in range(len(message)):
		encrypted_list.append(encrypt(ord(message[i]),n,e))
	return encrypted_list

#Decryption of a list of ciphers
#Returns the original message
def decrypted_message(encrypt_list,d,n):
	original_message = ''
	for i in range(len(encrypt_list)):
		original_message +=chr(decrypt(encrypt_list[i],d,n))
	return original_message 
