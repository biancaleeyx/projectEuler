"""
Project Euler Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# Set largest number.
number = 10001

# Initialise null prime list.
primes = []
# Initialise prime parser.
n = 2

while len(primes) < number:
    # Initialise non-prime counter.
    counter = 0

    for prime in primes:
        if n % prime == 0:
            counter += 1
            break

    # Add prime if no division occurred.
    if counter == 0:
        primes.append(n)

    # Parse next number.
    n += 1

print(primes[-1])
