"""
Project Euler Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum
is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# Set largest number.
number = 100

# Initialise sum of squares, sum.
sumOfSquares = 0
Sum = 0

for n in range(number+1):
    sumOfSquares += n**2
    Sum += n

print(abs(sumOfSquares - Sum**2))
