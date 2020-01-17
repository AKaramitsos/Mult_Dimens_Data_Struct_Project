# we have 2 lines: L1 and L2
# there is a set of p_n points on L1 and a set of q_n points on L2
# there is a set of s_n lines that connect L1 and L2
# s_i = s(p_i, q_i)
# the space between L1 and L2 is divided into R_n areas
# R_0 is the first area above the first line s_1 and so on
# we search for the area that containts the point p
# we use binary search so we get time O(logn)

#!/usr/bin/env python3
import sys
import os
import random

# Define the lines and their points
# Let's assume 20 points for simplicity
n = 20
# x coordinate is the same for all points because the lines are vertical
# L1
L1_px = 2
L1_py = [random.randint(0,101) for i in range(20)] # 20 random numbers from 0 to 100
L1_py.sort(reverse = True) # reverse sort because p_0 must have the highest y value

# L2
L2_px = 8
L2_py = [random.randint(0,101) for i in range(20)]
L1_py.sort(reverse = True)

# Function to find the area of point p(x, y)
def geom_bin_search_plane(x, y):
    top = 1
    bottom = n
    middle = (1 + n) // 2 # to get integer result
    
    while bottom > top + 1:
        if y > L1_py[middle] + (L2_py[middle] - L1_py[middle])*(x - L1_px) // (L2_px - L1_px):
            bottom = middle
        else:
            top = middle

        middle = (top + bottom) // 2

    print("The point p is in area R",middle-1)

# Calling the function with: 2 <= x <= 8 for the point
# to be between lines L1 and L2 and any positive value for y
geom_bin_search_plane(4, 80)