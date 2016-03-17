"""
Project Euler Problem 16: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

# Set power.
power = 1000

# Find digits of power.
digits = list(str(2**power))

# Find sum of digits.
digitSum = 0
for digit in digits:
    digitSum += int(digit)

# Output sum of digits.
print(digitSum)
