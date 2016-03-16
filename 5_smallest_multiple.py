"""
Project Euler Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import numpy as np

# Set largest number.
number = 20

# Initialise list of factors.
factors = np.arange(number+1)

# Simplify factors, dividing by smaller multiples.
for m in range(len(factors)):
    if factors[m] != 0:
        # Only deal with larger numbers.
        for n in range(m+1, len(factors)):
            if factors[n] % factors[m] == 0:
                factors[n] /= factors[m]

# Calculate LCM, output.
lcm = 1
for factor in factors:
    if factor != 0:
        lcm *= factor

print(lcm)
