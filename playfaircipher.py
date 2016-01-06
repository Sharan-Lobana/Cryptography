
def isCharRepeated(string):
	string = string.lower()
	count = {}
	for char in string:
		if count.has_key(char):
			return True
		else:
			count[char] = 1
	return False

def find(key_array,char):
	for i in range(5):
		for j in range(5):
			if key_array[i][j] == char:
				return (i,j)
	return (-1,-1)

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

	alphabets = 'abcdefghiklmnopqrstuvwxyz' #excluding 'j'

	#Declare the key matrix
	key = [['' for x in range(5)] for y in range(5)]
	i = -1
	length = len(enter_key)

	for j in range(length):
		if j%5 == 0:
			i+= 1
		# Character 'j' in the enter_key will map to 'i' in the key matrix
		if enter_key[j] != 'j':
			key[i][j%5] = enter_key[j]
		else:
			key[i][j%5] = 'i'
	index = length%5

	remaining = 25 - length
	pos = 0
	while remaining != 0:
		if alphabets[pos] not in enter_key:
			if index%5 == 0:
				i+= 1
			key[i][index%5] = alphabets[pos]
			index += 1
			remaining -= 1
		pos+=1
		if pos>25:
			break
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
	
