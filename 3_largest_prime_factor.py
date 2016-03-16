"""
Project Euler Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import numpy as np

number = 600851475143

# Initialise empty np.array.
primes = np.zeros(0)

# Ignore 0, 1; not primes.
for n in range(2, number):

    if number % n == 0:
        counter = 0
        for prime in primes:
            if n % prime == 0 and counter == 0:
                counter += 1
        if counter == 0:
            np.append(primes, n)

# Output largest prime.
print(primes[-1])
