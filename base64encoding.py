#Python implementation of base 64 encoding

def mapping(n):
	if 0<=n<=25:
		return chr(n+65)
	elif 26<=n<=51:
		return chr(n+71)
	elif 52<=n<=61:
		return str(n-52)
	elif n == 62:
		return '+'
	return '/'

def reverse_mapping(n):
	if 48<=n<=57:
		return n+4
	elif 65<=n<=90:
		return n-65
	elif 97<=n<=122:
		return n-71
	elif n==43:
		return 62
	return 63

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return str(digits[::-1])

def encode(message):
	length = len(message)
	binary_stream = ''
	append_value = ''

	for i in range(length):
		binary_stream = binary_stream + '{0:08b}'.format(ord(message[i]))

	if length%3==1:
		binary_stream = binary_stream + '0000'
		append_value = '=='
	elif length%3==2:
		binary_stream = binary_stream + '00'
		append_value = '='

	num_encoded_characters = len(binary_stream)/6
	encoded_message = ''

	for i in range(num_encoded_characters):
		encoded_message = encoded_message + mapping(int(binary_stream[6*i:6*(i+1)],base=2))
	
	encoded_message = encoded_message + append_value
	return encoded_message
def decode(enc):
	num_of_blocks = len(enc)/4
	original_stream = ''
	if num_of_blocks > 1:
		for i in range(4*(num_of_blocks-1)):
			char = reverse_mapping(ord(enc[i]))
			original_stream = original_stream + '{0:06b}'.format(char)
	if enc[-1]=='=':
		original_stream = original_stream + '{0:06b}'.format(reverse_mapping(ord(enc[-4])))
		original_stream = original_stream + '{0:06b}'.format(reverse_mapping(ord(enc[-3])))
		if enc[-2]!='=':
			original_stream = original_stream + '{0:06b}'.format(reverse_mapping(ord(enc[-2])))
			original_stream = original_stream[:-2]
		else:
			original_stream = original_stream[:-4]
	else:
		for i in range(4):
			original_stream = original_stream + '{0:06b}'.format(reverse_mapping(ord(enc[-4+i])))
	decoded_message = ''
	for i in range(len(original_stream)/8):
		decoded_message += chr(int(original_stream[8*i:8*(i+1)],base=2))
	return decoded_message

