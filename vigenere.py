#Python implementation of Vigenere cipher
from utils import alignment 

class Vigenere:
	'''The Vigenere Cipher is shifted Caesar Cipher 
	in which the key length is equal to message length
	and each plaintext character is shifted by an amount 
	decided by the corresponding character in the key'''
	
	def __init__(self,paraphrase="Thisistheparaphraseforkeygeneration"):
		self.key = paraphrase

	def set_key(self,string):
		self.key = string

	def encipher(self,message,key=None):
		if key==None:
			key=self.key
		message = message.replace(' ','')
		(filtered_message,aligned_key) = alignment(message,key)
		cipher = ''
		l2 = len(filtered_message)
		for i in range(l2):
			cipher += chr((ord(filtered_message[i])+ord(aligned_key[i]) -130)%26 + 65)
		return cipher

	def decipher(self,cipher,key=None):
		if key==None:
			key = self.key
		(cipher,aligned_key) = alignment(cipher,key)
		l2 = len(cipher)
		message = ''
		for i in range(l2):
			message += chr((ord(cipher[i]) - ord(aligned_key[i]) -130)%26 + 65)
		return message