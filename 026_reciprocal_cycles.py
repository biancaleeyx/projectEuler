"""
Project Euler Problem 26: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10 = 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import numpy as np

# Set largest value of d.
maxNum = 1000

# Long division; Python does not store true fractions, only binary approximations.
def recurringLength(d):
    print("Processing 1/{}...".format(d))
    length = 0

    # Avoid getting stuck at non-linear recurrance cases like 1/6 = 0.1(6) by checking if remainder has already been computed in list.
    remainders = []
    while (10**length) % d not in remainders:
        remainders.append((10**length) % d)
        length += 1
    return length - remainders.index((10**length) % d)


# Initialise variables.
dMax = 0
recurMax = 0

for d in range(2, maxNum):
    recurLength = recurringLength(d)
    if recurLength > recurMax:
        recurMax = recurLength
        dMax = d
        print("Current longest recurrant length of {} from 1/{}.".format(recurMax, dMax))

print(dMax)
