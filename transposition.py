#Implementation of transposition block cipher

from utils import generate_key_transposition,generate_random_string

#Block size = 25
def transpose(block_array,key):
	string =''
	for i in range(5):
		for j in range(5):
			string += block_array[j][int(key[i])]
	return string


def encipher(message,key=None):
	supplied = True
	#If the key is not supplied generate the key
	if key==None:
		supplied = False
		key = generate_key_transposition()

	message = message.replace(' ','')
	length = len(message)

	#If the message length is not a multiple of 25
	if length%25:
		additional_characters = 25 - length%25
		#Generate a random string of additonal characters
		append_string = generate_random_string(additional_characters)
		message += append_string
	#number of blocks with given block size
	num_iters = len(message)/25

	block_array = [['' for x in range(5)] for x in range(5)]
	#Index of character in plaintext
	index = 0
	cipher = ''

	for x in range(num_iters):
		for i in range(5):
			for j in range(5):
				block_array[i][j] = message[index]
				index +=1
		#Append the transposed plaintext to the cipher
		cipher += transpose(block_array,key)

	if supplied:
	#Return the cipher with the number of additional appended characters
		return (cipher,-length%25)
	#If the key is not supplied,return the key for deciphering
	return (cipher,-length%25,key)

def decipher(cipher,key,additional=0):
	length = len(cipher)
	block_array = [['' for x in range(5)] for x in range(5)]
	plaintext = ''
	#Number of blocks with additional block size
	num_iters = length/25
	#Index of character in cipher
	index = 0
	for x in range(num_iters):
		for i in range(5):
			for j in range(5):
				#Construct the block array
				block_array[j][key[i]] = cipher[index]
				index += 1

		#Append each row of block array to plaintext
		for i in range(5):
			plaintext += ''.join(block_array[i])
	#Truncate any additional characters in the plaintext
	if additional:
		plaintext = plaintext[:-additional]
	return plaintext