"""
Project Euler Problem 67: Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether!
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
"""

# Code adapted from 018_maximum_path_sum_i.py.

import numpy as np

# Parse triangle numbers.
triangleList = []
with open('imports/p067_triangle.txt') as f:
  for triangleString in f:
    triangleList.append(list(map(int, triangleString.split(' '))))

# Find number of lines in triangle.
linesNum = len(triangleList[-1])

# Start from last line. Choose between side to side numbers (keep larger). Decrease elements linearly by summation.
for lineNum in range(linesNum-1, 0, -1):
  for k in range(len(triangleList[lineNum])-1):
    triangleList[lineNum-1][k] += max(triangleList[lineNum][k], triangleList[lineNum][k+1])

print(triangleList[0][0])
