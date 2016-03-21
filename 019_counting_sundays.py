"""
Project Euler Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

   -1 Jan 1900 was a Monday.
   -Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
   -A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# 1900 is a leap year.

# Day on first date, count Sunday as 0, Monday as 1, and so on.
day = 366 % 7 + 1

# Set days in months.
monthDays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Initialise variable that counts number of sundays.
sundays = 0
# Initialise variable to take into account leap years.
yearFirst = 1901
yearLast = 2000

for year in range(yearFirst, yearLast+1):
	for month in monthDays:
		# Ignore last month of last year.
		if month != 12 or year != yearLast:
			# Check if leap year.
			if month == 2 and (year - 1900) % 4 == 0:
				day += 1
			day += monthDays[month]
			day = day % 7
			if day == 0:
				sundays += 1

print(sundays)
