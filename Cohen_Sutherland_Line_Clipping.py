# the algorithm divides the space in 9 regions
# the center region is the visible one and it's called the viewport
# the lines outside the viewport are removed
# the lines that have a part of them inside the viewport are clipped
# each line endpoint has a 4 bit outcode
# the outcode determines the relative position to the viewport
# |= is the bitwise OR and assign operation
# and is for boolean comparisons
# & is for bitwise comparisons

#!/usr/bin/env python3
import sys
import os

# Define outcodes
INSIDE = 0 # 0000
LEFT = 1   # 0001
RIGHT = 2  # 0010
BOTTOM = 4 # 0100
TOP = 8    # 1000

# Define viewport position
x_min = 5.0
x_max = 10.0 
y_min = 5.0
y_max = 10.0

# Function to calculate the outcode of a line endpoint
def calculate_outcode(x, y):
    outcode = INSIDE
    
    if x < x_min:
        outcode |= LEFT
    elif x > x_max:
        outcode |= RIGHT
    
    if y < y_min:
        outcode |= BOTTOM
    elif y > y_max:
        outcode |= TOP    

    return outcode


# Function to clip a line from P0 to P1
def coh_suth_line_clipping(x0, y0, x1, y1):
    outcode0 = calculate_outcode(x0, y0)
    outcode1 = calculate_outcode(x1, y1)
    accept = False

    while True:

        # If the whole line is inside the viewport
        if (outcode0 == 0) and (outcode1 == 0):
            accept = True
            break # to exit while loop
        # If the whole line is outside the viewport
        elif (outcode0 & outcode1) != 0:
            break
        # If only part of the line is inside the viewport
        else:
            # Chose the endpoint of the line that's outside the viewport
            if outcode0 != 0:
                outcode = outcode0
            else:
                outcode = outcode1
            
            # Find the point(x,y) on the viewport border
            if outcode & TOP:
                x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
                y = y_max
            elif outcode & BOTTOM:
                x = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
                y = y_min
            elif outcode & RIGHT:
                y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
                x = x_max
            elif outcode & LEFT:
                y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
                x = x_min

            # Replace the point outside the viewport with point(x,y)
            if outcode == outcode0:
                x0 = x
                y0 = y
                outcode0 = calculate_outcode(x0, y0)
            else:
                x1 = x
                y1 = y
                outcode1 = calculate_outcode(x1, y1)

    # Trivial accept
    if accept:
        print("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x0,y0,x1,y1))

    # Trivial reject
    else:
        print("Line rejected")

# Trivial accept line
#coh_suth_line_clipping(6, 6, 9, 9)

# Trivial reject line
#coh_suth_line_clipping(2, 12, 12, 12)

# Clipped line
coh_suth_line_clipping(6, 6, 13, 8)