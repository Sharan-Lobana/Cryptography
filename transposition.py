from utils import generate_key_transposition,generate_random_string

def transpose(block_array,key):
	string =''
	for i in range(5):
		for j in range(5):
			string += block_array[j][int(key[i])]
	return string


def encipher(message,key=None):
	if key==None:
		key = generate_key_transposition()
	message = message.replace(' ','')
	length = len(message)
	if length%25:
		additional_characters = 25 - length%25
		append_string = generate_random_string(additional_characters)
		message += append_string
	num_iters = len(message)/25

	block_array = [['' for x in range(5)] for x in range(5)]
	index = 0
	cipher = ''

	for x in range(num_iters):
		for i in range(5):
			for j in range(5):
				block_array[i][j] = message[index]
				index +=1
		cipher += transpose(block_array,key)
	return (cipher,-length%25)

def decipher(cipher,key,additional=0):
	length = len(cipher)
	block_array = [['' for x in range(5)] for x in range(5)]
	plaintext = ''
	num_iters = length/25
	index = 0
	for x in range(num_iters):
		for i in range(5):
			for j in range(5):
				block_array[j][key[i]] = cipher[index]
				index += 1
		for i in range(5):
			plaintext += ''.join(block_array[i])
	if additional:
		plaintext = plaintext[:-additional]
	return plaintext