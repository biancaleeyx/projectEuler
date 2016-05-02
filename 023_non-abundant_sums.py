"""
Project Euler Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot 
be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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

print(__file__ + " is running...")

# Set max number for brute forcing.
maxNum = 28123

# Create list of abundant numbers.
abundants = []
for number in range(1, maxNum):
	if sumDivisors(number) > number:
		abundants.append(number)
abundants = np.array(abundants)

print("List of abundant numbers created.")

integerSum = 0
for number in range(maxNum+1):
	abundantSum = False
	for abundant in np.nditer(abundants):
		if abundant <= number-abundants[0]:
			if number-abundant in abundants:
				abundantSum = True
				break
		else:
			break
	if not abundantSum:
		integerSum += number
		print("{} is a non-abundant sum. New total: {}.".format(str(number), str(integerSum)))

print("Sum of positive integers which are non-abundant sums is {}.".format(integerSum))
print(__file__ + " has finished running.")
