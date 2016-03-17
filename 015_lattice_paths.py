"""
Project Euler Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import numpy as np

# Set grid size.
gridSize = 20

# Number of combinations for 20 down, 20 right.
print(int(np.math.factorial(gridSize*2) / np.math.factorial(gridSize)**2))
