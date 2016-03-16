"""
Project Euler Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Initialise sum variable.
x = 0

for n in range(1000):
    # Find all numbers that are multiples of 3, 5, or 3 and 5.
    if n % 3 == 0 or n % 5 == 0:
        # Add to initialised variable.
        x += n

# Output desired sum.
print(x)