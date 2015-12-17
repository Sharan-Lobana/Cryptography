#Python implementation of the Rabin-Karp algorithm 
#for single-pattern search

#The hash value is multiplication of the 
#ascii values of individual characters
import math
LARGE_PRIME = 1000000007
SMALL_PRIME = 127
def rolling_hash1(s,first_time,start_index,length,prev_value):
	if first_time == 1:
		value = 1
		for i in range(length):
			value *= ord(s[i])-94 
			# value %= LARGE_PRIME
		return value 
	temp = ord(s[start_index-1])-94
	return_value = ((prev_value//temp)*(ord(s[start_index+length-1])-94))
	# %LARGE_PRIME
	# print("The return value of hash_function is "+str(return_value))
	return return_value

def rolling_hash2(s,first_time,start_index,length,prev_value):
	# value = 0
	# reverse_s = s[::-1]
	# for i in range(len(s)):
	# 	value
	return 1
	
def hash_value(string,first_time,start_index,length,prev_value,selector=0):
	if selector == 0:
		return rolling_hash1(string,first_time,start_index,length,prev_value)
	return rolling_hash2(string,first_time,start_index,length,prev_value)


def Rabin_Karp(string,pattern):
	m = len(pattern)
	# print("The length of pattern is " + str(m))
	n = len(string)
	# print("The length of string is " + str(n))
	hp = hash_value(pattern,1,0,m,prev_value=0)
	# print("The first time value for pattern is "+str(hp))
	hs = hash_value(string,1,0,m,prev_value=0)
	# print("The first time value for string is "+str(hs))
	for j in range(1,n-m+1):
		if hs == hp:
			# print("The hash values are equal at " + str(j))
			# print("The substing is "+string[j-1:j+m-1])
			if string[j-1:j+m-1] == pattern:
				return j-1
		hs = hash_value(string,0,j,m,hs)
	if hs == hp:
		if string[-m:] == pattern:
			return n-m
	return -1