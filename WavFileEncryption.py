#.wav audio file encryption and decryption
#using RC4 stream cipher

import wave
import rc4stream as r
from bitstring import BitArray

#Utility function to convert integer to hexadecimal
def int_to_hex(integer):
	dic = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
	if 0<= integer<= 9:
		return str(integer)
	else: return dic[integer]

#Generate the state vector for RC4 encryption 
#from the user supplied string
def generate_state_vector(string):
	bits_128 = r.generate_key(string)
	t_vec = r.initialize_T_vector(bits_128)
	s_vec = r.initialize_S_vector()
	s_vec = r.key_scheduling(s_vec,t_vec)
	return s_vec

#Encrypt a given .wav audio file with given state vector s
def encrypt_from_file(filename,s):
	f = wave.open(filename,'rb')
	#Gather metadata about the .wav file

	params = f.getparams()
	num_frames = params[3]
	#Extract the byte_stream
	byte_stream = f.readframes(num_frames)
	a = BitArray(bytes=byte_stream)
	bit_stream = a.bin 
	cipher,s= r.encipher(bit_stream,s,True)
	f.close()

	#The parameters are required for setting 
	#the metadata for decrypted file
	return cipher,s,params

#Pass the name of .wav file to which you want to save the audio
def decrypt_to_file(cipher,s,params,filename='new_file.wav'):
	f = wave.open(filename,'wb')
	#Set the params of the files
	f.setparams(params)
	original_bit_stream = r.decipher(cipher,s,True)
	bits_to_wavfile(original_bit_stream,f)

def bits_to_wavfile(bitstream,fileobject):
	byte_stream = ''
	for i in range(len(bitstream)/8):
		eight_bits = bitstream[8*i:8*(i+1)]
		four_bits1 = eight_bits[:4]
		four_bits2 = eight_bits[4:]
		integer1 = int(four_bits1,base=2)
		integer2 = int(four_bits2,base=2)
		hexadecimal1 = int_to_hex(integer1)
		hexadecimal2 = int_to_hex(integer2)
		byte_stream += (hexadecimal1+hexadecimal2).decode('hex')
	fileobject.writeframes(byte_stream)
	fileobject.close()


