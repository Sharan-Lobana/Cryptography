#Implementation of SHA-1 algorithm

from numpy import binary_repr

#Utility didctionary for binary to hex mapping
bin_to_hex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5'\
,'0110':'6','0111':'7','1000':'8','1001':'9','1010':'a'\
,'1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}

#Utility function for left-rotation of bits
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

#The second argument specifies whether to return binary or hexadecimal hash
def sha1(message,bin=False):

	#Initialize the variables
	h0 = 0x67452301
	h1 = 0xefcdab89
	h2 = 0x98badcfe
	h3 = 0x10325476
	h4 = 0xc3d2e1f0

	#Convert the message to binary
	binary_message = ''.join(format(ord(x),'b') for x in message)

	#Append 1 (NSA Specialists probably did this for fun :P )
	binary_message = binary_message + '1'

	length = len(binary_message)
	if length%512 != 448:
		x = length%512
		if x < 448:
			while x != 448:
				binary_message = binary_message + '0'
				x += 1
		else :
			while x != 960:
				binary_message = binary_message + '0'
				x += 1

	#Append the 64 bit length of original message to 
	#modified binary representation of message
	append_value = binary_repr(length,width=64)
	binary_message = binary_message + append_value

	#Count the number of 512 bit chunks
	num_chunks = len(binary_message)//512

	#for each chunk
	for i in range(num_chunks):

		#Pick up a chunk of message 512 bit long
		chunk = binary_message[512*i:512*(i+1)]
		list_of_words = []

		#Break the chunk into 16 32 bit words
		for j in range(16):
			list_of_words.append(chunk[32*j:32*(j+1)])

		# #debugging
		# print list_of_words

		list_of_words = [int(x,base=2) for x in list_of_words]

		# #debugging
		# print list_of_words

		#extend the 16 words into 80 words of length 32 bits
		for k in range(16,80):
			value_to_append = (list_of_words[k-3]^list_of_words[k-8]^list_of_words[k-14]^list_of_words[k-16])
			
			#Perform a leftrotation
			list_of_words.append(rol(value_to_append,1,32))

		#Initialize the hash value for this chunk
		a = h0
		b = h1
		c = h2
		d = h3
		e = h4

		#Main loop
		for j in range(0,80):
			if 0 <= j <= 19:
				f = (b & c) | ((~b) & d)
				k = 0x5a827999
			elif 20 <= j <= 39:
				f = b ^ c ^ d
				k = 0x6ed9eba1
			elif 40 <= j <= 59:
				f = (b & c) | (b & d) | (c & d)
				k = 0x8f1bbcdc
			else:
				f = b ^ c ^ d
				k = 0xca62c1d6

			temp = rol(a,5,32) + f + e + k + list_of_words[j]
			temp = temp%0x100000000
			
			e = d
			d = c
			c = rol(b,30,32)
			b = a
			a = temp

		#Add this chunk's hash to the result so far
		h0 = h0 + a
		h1 = h1 + b
		h2 = h2 + c
		h3 = h3 + d
		h4 = h4 + e

		#Take modulus 2**32
		h0 = h0%0x100000000
		h1 = h1%0x100000000
		h2 = h2%0x100000000
		h3 = h3%0x100000000
		h4 = h4%0x100000000

	#Convert each part to binary
	h0 = binary_repr(h0,width=32)
	h1 = binary_repr(h1,width=32)
	h2 = binary_repr(h2,width=32)
	h3 = binary_repr(h3,width=32)
	h4 = binary_repr(h4,width=32)

	bin_hash = str(h0)+str(h1)+str(h2)+str(h3)+str(h4)
	hex_hash = ''
	for i in range(40):
		hex_hash = hex_hash + bin_to_hex[bin_hash[4*i:4*(i+1)]]

	#If binary value is needed
	if bin:
		return (bin_hash,hex_hash)
		
	#If only hexadecimal id needed, This is default
	return hex_hash