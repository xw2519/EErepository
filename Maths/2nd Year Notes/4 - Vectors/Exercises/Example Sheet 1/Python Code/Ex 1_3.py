"""
Ex 1.py

Plot the following 2D scalar fields using Matlab, and sketch the equipotential lines.
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

"""
Surface Plot
"""
def fun(x, y):
    return np.arctan(y/x)

fig1 = plt.figure ()
ax1 = fig1.add_subplot (111 , projection ='3d')
x = y = np.arange ( -3.0, 3.0, 0.05)
X, Y = np.meshgrid (x, y)
zs = np.array (fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape (X.shape)

ax1.plot_surface (X, Y, Z)

ax1.set_xlabel ('X Label')
ax1.set_ylabel ('Y Label')
ax1.set_zlabel ('Z Label')

"""
Contour Plot
"""
fig2 = plt.figure (figsize =(6 ,5))
left, bottom, width, height = 0.1 ,0.1 ,0.8 ,0.8
ax2 = fig2.add_axes ([ left , bottom , width , height ])

xlist = np. linspace ( -5.0 ,5.0 ,100)
ylist = np. linspace ( -5.0 ,5.0 ,100)

X, Y = np. meshgrid (xlist , ylist)

Z3 = np.arctan(Y/X) # Z(x,y) = tan^{-1}(y/x)
cp = ax2.contour (X, Y, Z3)
ax2.clabel (cp , inline =True , fontsize =10)

ax2.set_title ('Scalar fields')

plt.show () # Show the plots