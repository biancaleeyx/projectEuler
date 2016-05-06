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

while counter <= len(combinationList)-1:
	for coin in set(combinationList[counter]):
		if coin == 1:
			continue
		else:
			combinationTemp = copy.deepcopy(combinationList[counter])
			combinationTemp.remove(coin)
			for coinType in coins[:np.where(coins==coin)[0][0]][::-1]:
				combination = copy.deepcopy(combinationTemp)
				combination.append(coinType)

				while sum(combination) < total:
					for coinType in coins[:np.where(coins==coin)[0][0]][::-1]:
						if coinType <= total - sum(combination):
							combination.append(coinType)
							break

				combination.sort()
				if sum(combination) != total:
					raise ValueError("Sum of combination is not equivalent to the desired total.")

				if combination not in combinationList:
					combinationList.append(combination)
					coinString, countString = np.unique(np.array(combination), return_counts=True)
					print("Combination #{}: {} cents * {}, respectively.".format(len(combinationList), coinString, countString))
	counter += 1

print("Number of ways to form £2: {}.".format(len(combinationList)))
