"""
Ex 1.py

Plot the following 2D scalar fields using Matlab, and sketch the equipotential lines.
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random


"""
Contour Plot
"""
fig2 = plt.figure (figsize =(6 ,5))
left, bottom, width, height = 0.1 ,0.1 ,0.8 ,0.8
ax2 = fig2.add_axes ([ left , bottom , width , height ])

xlist = np. linspace ( -5.0 ,5.0 ,100)
ylist = np. linspace ( -5.0 ,5.0 ,100)

X, Y = np. meshgrid (xlist , ylist)

Z3 = X # Z(x,y) = x
cp = ax2.contour (X, Y, Z3)
ax2.clabel (cp , inline =True , fontsize =10)

ax2.set_title ('Scalar fields')

plt.show () # Show the plots