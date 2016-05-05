"""
Project Euler Problem 31: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

import numpy as np

# Set sum to be made, using whole numbers i.e. pennies.
total = 200

# Define possible set.
coins = np.array([1, 2, 5, 10, 20, 50, 100, 200])
coinsList = []

# Create dictionary of number of ways to create amounts for each coin.
coinsDict = {1: 1}

# Find number of ways for each coin, building up from the smallest.
for i in range(1, len(coins)):
	coinLarger = coins[i]
	coinSmaller = coins[i-1]
	coinList = []
	while coinLarger != 0:
		num = coinLarger//coinSmaller
		coinLarger = coinLarger%coinSmaller
		coinSmaller = coins[np.where(coins==coinSmaller)[0][0]-1]
		coinList.append(num)
	coinsList.append(coinList)
	print("Simplest combination for coin of value {} is {}.".format(coins[i], coinList))

	# Calculate combination numbers.
	coin = coins[i]
	coinsDict[coin] = 1
	
	coinsType = (coins[i-len(coinList):i])[::-1]
	print("Number of coins for each type of coin, {}, is {} respectively.".format(coinsType, coinList))

	for coinType, count in zip(coinsType, coinList):
		coinsDict[coin] += np.math.factorial(count*coinsDict[coinType])/(np.math.factorial(count)*np.math.factorial(count*(coinsDict[coinType]-1)))

	print("The number of combinations for coin of value {} is {}.".format(coin, int(coinsDict[coin])))
	print()
