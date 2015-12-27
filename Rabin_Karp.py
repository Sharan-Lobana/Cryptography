#Python implementation of the Rabin-Karp algorithm 
#for single-pattern search

#The hash value is multiplication of the 
#ascii values of individual characters

#Suggestions for other rolling hash functions is highly appreciated

import math
# LARGE_PRIME = 1000000007
# SMALL_PRIME = 127
def rolling_hash1(s,first_time,start_index,length,prev_value):
	if first_time == 1:
		value = 1
		for i in range(length):
			value *= ord(s[i])-94 
		return value 
	temp = ord(s[start_index-1])-94
	return_value = ((prev_value//temp)*(ord(s[start_index+length-1])-94))
	return return_value
	
def hash_value(string,first_time,start_index,length,prev_value,selector=0):
	if selector == 0:
		return rolling_hash1(string,first_time,start_index,length,prev_value)
	return rolling_hash2(string,first_time,start_index,length,prev_value)


def Rabin_Karp(string,pattern):
	m = len(pattern)
	n = len(string)

	#Compute the hash value of the pattern and the first m characters of the string
	hp = hash_value(pattern,1,0,m,prev_value=0)
	hs = hash_value(string,1,0,m,prev_value=0)
	
	for j in range(1,n-m+1):

		#Look for pattern sub_string match if the hash values are equal
		if hs == hp:
			if string[j-1:j+m-1] == pattern:
				return j-1
		hs = hash_value(string,0,j,m,hs)
	if hs == hp:
		if string[-m:] == pattern:
			return n-m
	return -1