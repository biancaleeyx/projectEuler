"""
Project Euler Problem 31: Coin sums

In England the currency is made up of pound P and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).

It is possible to make P2 in the following way:

	1xP1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can P2 be made using any number of coins?
"""

import numpy as np
import copy
import math

# Set sum to be made in terms of p
total=200

# Possible coins
coins=[1, 2, 5, 10, 20, 50, 100, 200]

def ways(coins, total):
    if len(coins) == 0 or total<0:
        return 0
    if total == 0:
        return 1
    return ways(coins[:-1], total) + ways(coins, total-coins[-1])

print(ways(coins, total))