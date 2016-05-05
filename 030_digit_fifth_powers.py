"""
Project Euler Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

power = 5

# Find maximum possible number where the number of digits * 9**power < number with all digits 9.
digitsMax = 1
while digitsMax * 9**power >= int("9"*digitsMax):
	digitsMax += 1
maxNum = 10**digitsMax

print("Parsing to maximum possible number of {} for a power of {}.".format(10**digitsMax, power))

powerSum = 0

for number in range(2, maxNum):
	numberSum = 0
	for digit in str(number):
		numberSum += int(digit)**power

	if numberSum == number:
		powerSum += numberSum
		print("{} can be written as the sum of its digits to the power of {}.".format(number, power))

print("The sum of all such numbers is {}.".format(powerSum))
