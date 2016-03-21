#!/usr/bin/python

"""
Project Euler Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import numpy as np

def sumDivisors(number):
	"""
	Find sum of proper divisors of number by creating combinations from prime factors.
	:params number: int, positive.
	:return divisorSum: int.
	"""

	def primeFactorisation(number):
		"""
		Find prime factors.
		:params number: int.
		:return primeFactors: list of int, without [1].
		"""
		primeFactors = []
		for n in range(2, number):
		    # Check if number has been processed already.
		    while number % n == 0:
		        number /= n
		        primeFactors.append(n)
		    if number == 1:
		        break
		return primeFactors

	# Note: return_counts does not exist in Python 2.
	primes, counts = np.unique(np.array(primeFactorisation(number)), return_counts=True)

	# Form dictionary.
	primeDict = {}
	for prime, count in zip(primes, counts):
		primeDict[prime] = count

	# Calculate sum of divisors = product of sum of primes in powers (starting from 0).
	divisorSum = 1
	for prime in primeDict:
		count = primeDict[prime]
		powerSum = 0
		for power in range(count+1):
			powerSum += prime**power
		divisorSum *= powerSum
	# Exclude original number.
	divisorSum -= number

	return divisorSum

# Set maximum number.
maxNum = 10000

# Find amicable numbers.
amicables = []
for number in range(2, maxNum):
	if number not in amicables:
		dnumber = sumDivisors(number)
		if 0 < dnumber < maxNum:
			if number == sumDivisors(dnumber) and number != dnumber:
				amicables.append(number)
				amicables.append(dnumber)

# Find sum of amicable numbers.
amicableSum = 0
for amicable in amicables:
	amicableSum += amicable

print(amicableSum)
