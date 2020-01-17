# we have L lines: L1 to Ln
# there is a set of Pn points on an L line
# these points are where the Ln lines intersect with the L line
# the space between L1 and Ln is divided into Rn areas
# R0 is the first area above the first line L1 and so on
# we search for the area that containts the point P
# we use binary search so we get time O(logn)

#!/usr/bin/env python3
import sys
import os
import random

# Define the points that represent the Ln lines
# Let's assume 20 points for simplicity
n = 20
# x coordinate is the same for all points because the lines are vertical

# 20 random points where x == y for simplicity
Px = [random.randint(0,31) for i in range(20)]
Py = Px
Px.sort(reverse = True)
Py.sort(reverse = True)

# Function to find the area of point P(x, y)
def geom_bin_search_plane(x, y):

    top = 1
    bottom = n
    middle = (1 + n) // 2 # to get integer result
    
    while bottom > top + 1:
        if y > Py[middle]:
            bottom = middle
        else:
            top = middle

        middle = (top + bottom) // 2

    print("The point p is in area R",middle-1)

# only works for x == y
geom_bin_search_plane(8, 8)