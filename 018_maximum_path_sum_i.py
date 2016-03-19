"""
Project Euler Problem 18: Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""

import numpy as np

# Note: combinations = 2**(linesNum-1)

# Parse triangle numbers.
triangleString = \
                '75 \
                95 64 \
                17 47 82 \
                18 35 87 10 \
                20 04 82 47 65 \
                19 01 23 75 03 34 \
                88 02 77 73 07 63 67 \
                99 65 04 28 06 16 70 92 \
                41 41 26 56 83 40 80 70 33 \
                41 48 72 33 47 32 37 16 94 29 \
                53 71 44 65 25 43 91 52 97 51 14 \
                70 11 33 28 77 73 17 78 39 68 17 57 \
                91 71 52 38 17 14 91 43 58 50 27 29 48 \
                63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
                04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
triangleNum = list(map(int, triangleString.split()))

# Find number of lines in triangle.
linesNum = int(np.sqrt(float(len(triangleNum))*2.0 + 0.25) - 0.5)

# Form list of lists of ints in lines.
triangleList = []
counter = 0
for lineNum in range(1, linesNum+1):
	lineList = []
	for i in range(lineNum):
		lineList.append(triangleNum[counter])
		counter += 1
	triangleList.append(lineList)

# Parse through all routes, only remember by comparison.
total = triangleList[0][0]
totalMax = 0
index = 0
# Parse through lines.
for lineNum in range(1, linesNum):
	# Parse through numbers in lines.
	for index in range(index, index+2)
		number = triangleList[lineNum][index]
		total += number
		# Pick next number in index.
		# doesn't work cause 'total' is not reset for each combination.
