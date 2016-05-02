"""
Project Euler Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values 
of n, starting with n = 0.
"""

import numpy as np

def primeList(numMax=1000, primes=None, initialMax=None):
	"""
	Create list of primes up to a largest value.
	"""
	# if initialMax is not None:
	#	print("Expanding list of primes from {} to {}...".format(initialMax,numMax))

	if primes is None:
		# Initialise np.array.
		primes = np.arange(2, numMax)
	else:
		if initialMax is None:
			initialMax = primes[-1]
		np.concatenate((primes, np.arange(initialMax+1, numMax)))

	for prime in np.nditer(primes):
		if initialMax is None:
			multiple = 2*prime
		else:
			multiple = (initialMax//prime + 1) * prime
		while multiple < numMax:
			np.delete(primes, np.where(primes==multiple))
			multiple += prime
	
	# print("List of primes to {} created.".format(numMax))
	return primes

maxNum = 1000
initialMax = maxNum
primes = primeList(numMax=maxNum)

nMax = 0

for a in range(1-maxNum, maxNum):
	for b in np.nditer(primes):
		if b < maxNum:
			n = 0
			prime = True
			while prime:
				quadratic = n**2 + a*n + b
				if quadratic <= 0:
					prime = False
				elif quadratic in primes:
					n += 1
				elif quadratic < initialMax:
					prime = False
				else:
					# Update list of primes to the largest parsed number.
					primes = primeList(numMax=quadratic, primes=primes, initialMax=initialMax)
					initialMax = quadratic
					if quadratic in primes:
						n += 1
					else:
						prime = False

			# Update max variables if larger n primes reached.
			if n > nMax:
				nMax = n
				aMax = a
				bMax = b
				print("Current largest n is {} with a={} and b={}.".format(nMax, aMax, bMax))
		else:
			break

print("Product of coefficients of quadratic equation producing largest n of {}: {}.".format(nMax, aMax*bMax))
