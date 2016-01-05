#Python implementation of RSA encryption 
import random

def isPrime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

def modular_multiplicative_inverse(a,n):
	t = 0
	nt = 1
	r = n
	nr = a%n 
	if n < 0:
		n = -n
	if a < 0:
		a = n - (-a%n)
	while nr != 0:
		quot = (r/nr) | 0
		tmp = nt 
		nt = t = quot*nt 
		t = tmp
		tmp = nr 
		nr = r - quot*nr 
		r = tmp
	if r > 1:
		return -1
	if t < 0:
		t += n
	return t 

def random_prime(mini,maxi):
	p = random.randint(mini,maxi)
	if isPrime(p):
		return p
	else :
		return random_prime(mini,maxi)

def generate():
	p = random_prime(2,255) #8 bit
	q = random_prime(2,255) #8 bit
	n = p*q
	t = (p - 1)*(q - 1) # Totient 
	e = random_prime(2,t)
	d = modular_multiplicative_inverse(e,t)

	return {'public_key':[n,e],'private_key':d}

def encrypt(m,n,e):
	return pow(m,e,n)

def decrypt(mEnc,d,n):
	return pow(mEnc,d,n)