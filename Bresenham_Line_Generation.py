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
    D = 2*dy - dx # Slope error
    y = y0

    px.append(x0)
    py.append(y0)

    for x in range(x0, x1+1):
        xp.append(x)
        yp.append(y)
        # print("(",x ,",",y ,")\n")
        if D > 0:
            y = y + 1
            D = D - 2*dx

        D = D + 2*dy

    px.append(x)
    py.append(y)

    plt.grid(linestyle='--') # Add some -- for visual clarity
    plt.plot(px, py, 'ro-')
    plt.plot(xp, yp, 'ro')
    plt.show()

bresenham_line(1, 5, 6, 8) # Calling the function with 2 points
