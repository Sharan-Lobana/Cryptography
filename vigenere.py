#Python implementation of Vigenere cipher

def alignment(cipher,key):
	l1 = len(key)
	l2 = len(cipher)
	cipher = cipher.upper()
	key = key.upper()
	aligned_key = ''
	if l1 >= l2:
		aligned_key = key[:l2]
	else:
		repeatitions = l2/l1
	for i in range(repeatitions):
		aligned_key += key
	if (l2%l1) !=0:
		aligned_key +=key[:l2%l1]
	return (cipher,aligned_key)

def encipher(message,key="ABRACADABRA"):
	message = message.replace(' ','')
	(filtered_message,aligned_key) = alignment(message,key)
	print filtered_message 
	print aligned_key
	cipher = ''
	l2 = len(filtered_message)
	print l2
	for i in range(l2):
		cipher += chr((ord(filtered_message[i])+ord(aligned_key[i]) -130)%26 + 65)
	return cipher

def decipher(cipher,key="ABRACADABRA"):
	(cipher,aligned_key) = alignment(cipher,key)
	l2 = len(cipher)
	message = ''
	for i in range(l2):
		message += chr((ord(cipher[i]) - ord(aligned_key[i]) -130)%26 + 65)
	return message