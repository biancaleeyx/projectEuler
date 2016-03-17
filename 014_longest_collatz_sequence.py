"""
Project Euler Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import copy


def collatz(number):
    """
    Find next number in Collatz sequence.
    :param number: int.
    :return number1: int. next number in sequence.
    """
    if number % 2 == 0:
        number1 = number // 2
    else:
        number1 = 3*number + 1
    return number1


def collatzTerms(n):
    """
    Find number of terms through a recursive function.
    :param number: int.
    :return terms: int.
    """
    # Check if number has already been processed.
    if str(n) not in collatzDict:
        # Not processed, add to dictionary.
        collatzDict[str(n)] = collatzTerms(collatz(n)) + 1
    return collatzDict[str(n)]

# Set largest number possible.
numberMax = 999999
collatzDict = {'1': 1}
termsMax = 1

# Work down the chain, use dictionary.
for startingNum in range(1, numberMax+1):
    collatzTerms(startingNum)
    if collatzDict[str(startingNum)] > termsMax:
        startingMax = copy.deepcopy(startingNum)
        termsMax = collatzDict[str(startingNum)]

# Output longest chain's starting number.
print(startingMax)
