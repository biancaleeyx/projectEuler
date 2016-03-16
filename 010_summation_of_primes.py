"""
Project Euler Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy as np

# Set largest number.
number = 2000000

# Initialise np.array, zeros are primes, ones are not.
primes = np.zeros(number)

# Set 0, 1 to not prime.
primes[0] = 1
primes[1] = 1

for i in range(number):
    if primes[i] == 0:
        for multiple in range(2, number//i+1):
            if multiple*i <= number-1:
                # Ignore prime itself, set all multiples to not prime.
                primes[multiple*i] = 1

# Form np.array of primes from binary list.
primesIndices = np.where(primes == 0)

# Output sum of primes.
print(np.sum(primesIndices))
