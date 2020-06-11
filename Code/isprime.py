def isprime(num):
	isprime = False
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				isprime = False
				break
			else:
				isprime=True
	else:
		isprime = False
	return isprime