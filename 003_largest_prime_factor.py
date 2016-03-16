"""
Project Euler Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

number = 600851475143

for n in range(2, number):
    # Check if number has been processed already.
    while number % n == 0:
        number /= n
    if number == 1:
        print(n)
        break

