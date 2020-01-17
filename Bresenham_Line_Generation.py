# bottom left element is (0,0) with coordinates (x0,y0)
# x is the column and y is the row
# line is drawn from bottom left to top right

#!/usr/bin/env python3
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# First and last point lists
px = []
py = []
# Point lists
xp = []
yp = []

def bresenham_line(x0, y0, x1, y1):

    dx = abs(x1-x0)
    dy = abs(y1-y0)
    y = y0
    D = 2*dy - dx # Slope error

    px.append(x0)
    py.append(y0)

    while x0 < x1+1:

        plt.plot(x0, y, 'ro')

        if D > 0:
            #plt.plot(x, y, 'ro')
            if y != y1:
                y = y + 1
            D = D - 2*dx

        D = D + 2*dy
        if x0 != x1:
            x0 = x0 + 1

    px.append(x0)
    py.append(y)

    plt.grid(linestyle='--') # Add some -- on the figure for visual clarity
    plt.plot(px, py, 'ro-') # ro for red spheres as the points - for line
    plt.show()

bresenham_line(0, 1, 6, 4) # Calling the function with 2 points
