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

# Set sum to be made, using whole numbers i.e. pennies.
total = 200

# Define possible set.
coins = np.array([1, 2, 5, 10, 20, 50, 100, 200])

# Find list of combinations, unique.
combinationList = [[total]]
counter = 0

while [1]*total not in combinationList:
	combination = combinationList[counter]
	print("Processing combination of {}...".format(combination))
	for coin in set(combination):
		if coin == 1:
			continue
		else:
			combinationTemp = copy.deepcopy(combination)
			combinationTemp.remove(coin)
			combinationTemp.append(coins[np.where(coins==coin)[0][0]-1])

			while sum(combinationTemp) < total:
				for coinType in coins[::-1]:
					if coinType <= total - sum(combinationTemp):
						combinationTemp.append(coinType)
						break

			combinationTemp.sort()
			if sum(combinationTemp) != total:
				raise ValueError("Sum of combination is not equivalent to the desired total.")

			if combinationTemp not in combinationList:
				combinationList.append(combinationTemp)
				print("New combination: {}.".format(combinationTemp))
	counter += 1

print("Number of ways to form £2: {}.".format(len(combinationList)))
