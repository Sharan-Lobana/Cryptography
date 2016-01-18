#Implementation of Caesar substitution cipher

class Caesar:
	def __init__(self,key=16):
		self.key = key%26
		
