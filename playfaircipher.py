#Utility function to check repition of characters in keys
def isCharRepeated(string):
	string = string.lower()
	count = {}
	for char in string:
		if count.has_key(char):
			return True
		else:
			count[char] = 1
	return False

#Utility function to find the position of char in the key_array
def find(key_array,char):
	for i in range(5):
		for j in range(5):
			if key_array[i][j] == char:
				return (i,j)
	return (-1,-1)

#Function to generate the 5x5 key matrix from the user supplied key
def key_to_array(enter_key):
	enter_key = enter_key.lower()
	enter_key = enter_key.replace(' ','') #Remove whitespace in the keys

	# If the key contains repeated characters then it is invalid
	if isCharRepeated(enter_key) or len(enter_key)>26:
		print "Please chose a valid key"
		return None
	# The enter_key cannot have both 'i' and 'j' characters
	# since both are mapped to same cell and it will be repitition
	if 'i' in enter_key and 'j' in enter_key:
		print "The key cannot have both 'i' and 'j' characters"
		return None

	alphabets = 'abcdefghiklmnopqrstuvwxyz' #excluding 'j' since it maps to 'i'

	#Declare the key matrix
	key = [['' for x in range(5)] for y in range(5)]

	#Row index for the key_array 
	i = -1

	length = len(enter_key)

	for j in range(length):

		#Move to new row if current row if filled
		if j%5 == 0:
			i+= 1

		# Character 'j' in the enter_key will map to 'i' in the key matrix
		if enter_key[j] != 'j':
			key[i][j%5] = enter_key[j]
		else:
			key[i][j%5] = 'i'

	#The starting column of the remaining vacant key_array
	index = length%5

	#Remaining elements in the key_array
	remaining = 25 - length

	#Position of character in alphabets
	pos = 0

	#Fill in the remaining positions of the key_array 
	#using the characters in alphabets which are not in key
	while remaining != 0:
		#If the charcter is not in enter_key
		if alphabets[pos] not in enter_key:

			#Move to next row in key_array if current row is full
			if index%5 == 0:
				i+= 1

			#Assign the current character to given location in key_array
			key[i][index%5] = alphabets[pos]
			index += 1
			remaining -= 1
		pos+=1
		
	return key 

def encrypt(message,key_array):
	message = message.lower()
	message = message.replace(' ','')
	length = len(message)
	code = ''
	#If message is of odd length append 'x' at the end
	if length%2 ==1 :
		message += 'x'
	num_pairs = length/2
	for i in range(num_pairs):
		pair = message[2*i:2*(i+1)]
		pair = pair.replace('j','i')
		(i1,j1)=find(key_array,pair[0])
		(i2,j2) = find(key_array,pair[1])

		#If in the same column use the rightness property
		if (j1 == j2):
			code += key_array[i1][(j1+1)%5]
			code += key_array[i2][(j1+1)%5]

		#If in the same row use the belowness property
		elif(i1 == i2):
			code += key_array[(i1+1)%5][j1]
			code += key_array[(i1+1)%5][j2]

		#Else use the characters at the other diagonal of the rectangle 
		#whose one diagonal is represented by the two characters
		else:
			code += key_array[i1][j2]
			code += key_array[i2][j1]

	return code

#The decryption decodes 'j' characters as 'i' characters
#Hence the PlayFairCipher is not a perfect encryption decryption algorithm
#Since it doesn't maintain the integrity of the orignal message	
def decrypt(code,key_array):
	original_message =''
	num_pairs = len(code)/2
	for i in range(num_pairs):
		pair = code[2*i:2*(i+1)]
		(i1,j1)=find(key_array,pair[0])
		(i2,j2) = find(key_array,pair[1])

		#If in the same column use the reverse of rightness property
		if (j1 == j2):
			original_message += key_array[i1][(j1+4)%5]
			original_message += key_array[i2][(j1+4)%5]

		#If in the same row use the reverse of belowness property
		elif(i1 == i2):
			original_message += key_array[(i1+4)%5][j1]
			original_message += key_array[(i1+4)%5][j2]

		#Else use the characters at the other diagonal of the rectangle 
		#whose one diagonal is represented by the two characters
		else:
			original_message += key_array[i1][j2]
			original_message += key_array[i2][j1]

	return original_message
