"""
Project Euler Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import numpy as np

# Set variables.
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits = np.sort(np.array(digits))
permutationNum = 1000000

# Number of permutations of n numbers = n!
permutationNum -= 1
permutation = ''
while len(digits) != 0:
	digit = (permutationNum//np.math.factorial(len(digits)-1))
	permutation += str(digits[digit])
	permutationNum = permutationNum % np.math.factorial(len(digits)-1)
	digits = np.delete(digits, np.where(digits==digits[digit]))

print(permutation)
print(__file__ + " has finished running.")
