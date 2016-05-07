"""
Project Euler Problem 31: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

import numpy as np
import copy
import time

timeStart = time.clock()

print("{} is running...".format(__file__))

# Set sum to be made, using whole numbers i.e. pennies.
total = 200

# Define possible set.
coins = np.array([1, 2, 5, 10, 20, 50, 100, 200])

# Find list of combinations, unique.
combinationList = [[]]

# Create list of maximum number of coins of each type.
coinsMax = []
for coin in coins:
	coinsMax.append(total//coin)
coinsMax = np.array(coinsMax)
print("Variables set.")

# Create brute force combination of numbers of coins of each type.
for coinType, coinMax in zip(coins, coinsMax):
	print("Processing coin of value {}...".format(coinType))
	for combination in combinationList:
		if len(combination) > np.where(coins==coinType)[0][0]:
			break
		else:
			for coinNum in range(coinMax+1):
				combinationTemp = copy.deepcopy(combination)
				combinationTemp.append(coinNum)
				combinationList.append(combinationTemp)
			combinationList.remove(combination)
print("Generation of combination list complete. \nNow calculating number of ways...")

ways = 0
for combination in combinationList:
	waySum = 0
	for coinType, coinNum in zip(coins, combination):
		waySum += coinType*coinNum
	if waySum == total:
		ways += 1

print("Number of ways to form £2: {}.".format(ways))

timeEnd = time.clock()
print("Time taken: {:0.0f} minutes, {:0.0f} seconds.".format((timeEnd-timeStart)//60, (timeEnd-timeStart)%60))
