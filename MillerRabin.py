#Miller-Rabin implementation

def primality_test(p):
	probes = [2,3,5,7,11,13,17,23]	#The probes for a
	if any([p%a == 0 for a in probes]):return 0	#if p is divisble by a then not prime
	k,q = 0,p-1 
	while not q&1:
		q>>=1 
		k+=1 
	for a in probes:
		a_to_power_q = pow(a,q,p)
		if a_to_power_q == 1 or a_to_power_q == p-1 : continue
		a_to_power_jq = a_to_power_q
		flag = 0
		for j in range(k-1):
			a_to_power_jq = pow(a_to_power_jq,2,p)
			if a_to_power_jq == p-1:
				flag  = 1
				break
		if not flag: return 0
	probability_of_prime = 1 - 1.0/(4**len(probes))
	return probability_of_prime

def test_for_prime(p):
	probability = primality_test(p)
	if probability > 0:
		return 1
	return 0

def test(p):
	if p == 2 or p ==2 : return 1
	for i in range(2,int(round(pow(p,0.5)))+1):
		if p%i == 0: return 0
	return 1

def testing(num):
	for i in range(31,num+1):
		if test(i) != test_for_prime(i):
			print "The test failed for i = "+str(i)
		if (i%1000 == 0):
			print "The test has been successful for "+str(i)+" numbers"
