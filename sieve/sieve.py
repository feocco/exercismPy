def sieve(limit):
	composites = []
	primes = []

	for number in range(2,limit + 1):
		if number not in composites:
			primes.append(number)
		counter = 2
		value = 0
		while value < limit:
			value = number * counter
			composites.append(value)
			counter += 1
	
	return primes