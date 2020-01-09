# We are using the 8 part symmetry of a circle (45 degrees per octant)
# (0, 0) circle center
#

import numpy as np
import matplotlib.pyplot as plt

# Point lists
xp = []
yp = []

def bresenham_circle(xc, yc, r):

    x = 0
    y = r 
    D = 3 - 2 * r #D ecision parameter

    xp.append(xc+x) 
    xp.append(xc-x)
    xp.append(xc+x)
    xp.append(xc-x) 
    xp.append(xc+y)
    xp.append(xc-y)
    xp.append(xc+y)
    xp.append(xc-y)

    yp.append(yc+y) 
    yp.append(yc+y)
    yp.append(yc-y)
    yp.append(yc-y) 
    yp.append(yc+x)
    yp.append(yc+x)
    yp.append(yc-x)
    yp.append(yc-x)

    plt.plot(xp, yp, 'ro')
    plt.show()

    while x <= y:  
          
        x = x + 1

        if (D < 0):
            D = D + (4 * x) + 6
        else:
            D = D + 4 * (x - y) + 10
            y = y - 1

        # xp.append(x)
        # yp.append(y)

    plt.grid(linestyle='--') # Add some -- for visual clarity
    # plt.plot(xp, yp, 'ro')
    # plt.show()

# Calling the function passing the circle center and radius
bresenham_circle(4, 5, 3)