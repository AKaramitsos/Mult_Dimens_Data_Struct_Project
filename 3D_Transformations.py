# we have a point P(x, y) and we want to apply transformations on it
# for displacement we want to move the point by values dx and dy on the respective axis
# so we have P'(x', y') where x' = x + dx and y' = y + dy
# for shift we want to move the point by a value on a single only axis
# so we have P'(x', y) where x' = x + dx or P'(x, y') where y' = y + dy
# for rotation we want to rotare the point by angle 'theta' from axis origin (0, 0)

#!/usr/bin/env python3
import sys
import os
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Define our point's coordinates
Px = random.randint(0,11)
Py = random.randint(0,11)

def trans_displacement(x, y):
    x_n = Px + x
    y_n = Py + y

    plt.grid(linestyle='--') # Add some -- on the figure for visual clarity
    plt.plot(x_n, y_n, 'ro-') # ro for red spheres as the points - for line
    plt.plot(Px, Py, 'bo-') # blue for original position
    plt.show()

def trans_shift(x, y):
    x_s = Px * x
    y_s = Py * y

    plt.grid(linestyle='--') # Add some -- on the figure for visual clarity
    plt.plot(x_s, y_s, 'ro-') # ro for red spheres as the points - for line
    plt.plot(Px, Py, 'bo-') # blue for original position
    plt.show()

def trans_rotation(theta):
    x_r = math.cos(theta) * Px - math.sin(theta) * Py
    y_r = math.sin(theta) * Px - math.cos(theta) * Py

    plt.grid(linestyle='--') # Add some -- on the figure for visual clarity
    plt.plot(x_r, y_r, 'ro-') # ro for red spheres as the points - for line
    plt.plot(Px, Py, 'bo-') # blue for original position
    plt.show()

# calling with values to add to coordinates 
trans_displacement(5, 6)

# calling with values to multiply with the coordinates
trans_shift(2, 3)

# calling with angle theta of 10 degrees
trans_rotation(math.radians(10))