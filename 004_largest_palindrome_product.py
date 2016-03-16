"""
Project Euler Problem 4: Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
palindrome = []

# Start from largest possible 3-digit numbers.
for a in range(999, 100, -1):
    for b in range(999, 100, -1):
        product = a * b

        # Initialise non-palindromic counter.
        counter = 0

        # Test if product is a palindrome.
        string = str(product)
        for i in range(len(string)//2):
            if string[i] != string[-i-1] and counter == 0:
                counter += 1

        # Add palindrome to list if product is palindrome.
        if counter == 0:
            palindrome.append(product)

# Find largest palindrome.
print(max(palindrome))
