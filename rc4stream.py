#Python implementation of RC4 stream cipher

from SHA_1 import sha1 
def initialize_S_vector():
	return ['{0:08b}'.format(x) for x in range(0,256)]

def generate_key(key_string):
	return sha1(key_string,bin=True)[0][:128]

def initialize_T_vector(key):
	key_length =len(key)/8
	int_key = []
	for i in range(16):
		int_key.append(int(key[8*i:8*(i+1)],base=2))
	t_vector = []
	for i in range(256):
		t_vector.append(int_key[i%16])
	return t_vector

def key_scheduling(s_vector,t_vector):
	j = 0
	for i in range(256):
		j = (j+ int(s_vector[i],base=2) + t_vector[i]) % 256
		s_vector[i],s_vector[j] = s_vector[j],s_vector[i]
	return s_vector

def encipher(plaintext,s):
	copy = s[:]
	length = len(plaintext)
	i = 0
	j = 0
	cipher = ''
	index = 0
	while(index != length):
		i = (i+1)%256
		j = (j+int(s[i],base=2))%256
		#Dynamically change the state of pseudorandom number generator
		s[i],s[j] = s[j],s[i] 
		k = (int(s[i],base=2)+int(s[j],base=2))%256
		cipher += '{0:08b}'.format(ord(plaintext[index])^int(s[k],base=2))
		index += 1
	return cipher,copy

def decipher(cipher,s):
	length = len(cipher)/8
	i = 0
	j = 0
	plaintext = ''
	index = 0
	while(index != length):
		i = (i+1)%256
		j = (j+int(s[i],base=2))%256
		#Dynamically change the state of pseudorandom number generator
		s[i],s[j] = s[j],s[i] 
		k = (int(s[i],base=2)+int(s[j],base=2))%256
		plaintext += chr(int(cipher[8*index:8*(index+1)],base=2)^int(s[k],base=2))
		index += 1
	return plaintext