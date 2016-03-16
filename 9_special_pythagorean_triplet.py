"""
Project Euler Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# Set sum of a, b, c.
number = 1000

for b in range(number):
    for a in range(b):
        # Find c given that a + b + c = 1000.
        c = number - a - b

        # Proceed if c > b.
        if c > b:
            # Verify Pythagorean triplet. If true, output abc.
            if a**2 + b**2 == c**2:
                print(a*b*c)
                break
        else:
            # Stop parsing through a, c will never be < b.
            break
