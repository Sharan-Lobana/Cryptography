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