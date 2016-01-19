#Implementation of Caesar substitution cipher

class Caesar:
	
	def __init__(self,key=16):
		self.key = key%26
	def get_key():
		return self.key
		
	def encipher(plaintext):
		plaintext = plaintext.upper();
		cipher = ''
		for i in plaintext:
			cipher += chr((ord(i)+self.key)%26 + 65)
		return cipher
	
	def decipher(cipher):
		plaintext = ''
		for i in cipher:
			plaintext += chr((ord(i)-self.key)%26 + 65
		return plaintext
		
		
		
