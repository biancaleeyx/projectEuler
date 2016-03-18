"""
Project Euler Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
E.g. 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

# Set dictionary, spell.
strings = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
           11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
           18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
           70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 'and': 'and'}

# Calculate number of letters for each entry in dictionary, update dictionary as numbers.
numbers = {}
for number in strings:
    try:
        if number < 100:
            numbers[number] = len(strings[number])
    except TypeError:
        continue

# Set rules.
for n in range(1, 1001):
    if n not in numbers:
        if n < 100:
            numbers[n] = numbers[n - (n%10)] + numbers[n%10]
        elif n % 100 == 0 and n < 1000:
            numbers[n] = len(strings[100]) + numbers[n//100]
        elif n < 1000:
            numbers[n] = numbers[n - (n % 100)] + numbers[n % 100] + len(strings['and'])
        elif n == 1000:
            numbers[n] = len(strings[1000]) + numbers[n//1000]

# Calculate sum of numbers.
numberSum = 0
for n in range(1, 1001):
    numberSum += numbers[n]

print(numberSum)

"""
Ways to improve:
Find sum of letters in 1 to 99.
Multiply as necessary in hundreds. (One hundred and ..., two hundred and ..., ...)
"""
