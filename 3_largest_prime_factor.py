"""
Project Euler Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import numpy as np

number = 600851475143

# Create np.array of primes. 0 denotes prime, 1 denotes not prime.
primes = np.zeros(number)
primes[0] = 1
primes[1] = 1

for n in range(2, number):
    # Check if number has been processed already.
    if primes[n] == 0:
        times = n // number

        # Start from 2, don't change prime itself.
        for multiple in range(2, times):
            if primes[multiple*n] == 0:
                primes[multiple*n] = 1

# Create np.array of prime numbers.
primeIndices = np.where(primes == 0)

# Start searching for prime from largest, stop if prime is a factor of number.
for prime in reversed(primeIndices):
    if number % prime == 0:
        print(prime)
        break

