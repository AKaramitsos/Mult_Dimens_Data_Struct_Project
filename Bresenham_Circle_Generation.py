# We are using the 8 part symmetry of a circle (45 degrees per octant)
# (0, 0) circle center
#

import numpy as np
import matplotlib.pyplot as plt

# Point lists
xp = []
yp = []

def draw_circle(xc, yc, x, y):
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


def bresenham_circle(xc, yc, r):

    x = 0
    y = r 
    D = 3 - 2 * r # Decision parameter

    while y >= x:  
          
        draw_circle(xc, yc, x, y)
        x = x + 1

        if (D > 0):
            y = y - 1
            D = D + 4 * (x - y) + 10
        else:
            D = D + (4 * x) + 6
            draw_circle(xc, yc, x, y)

        #xp.append(x)
        #yp.append(y)

    plt.grid(linestyle='--') # Add some -- for visual clarity
    plt.plot(xp, yp, 'ro')
    plt.show()

# Calling the function passing the circle center and radius
bresenham_circle(50, 50, 30)