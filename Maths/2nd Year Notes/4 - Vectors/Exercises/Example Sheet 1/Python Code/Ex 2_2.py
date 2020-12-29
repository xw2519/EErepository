"""
Ex 2.py

Plot the following vector fields.
"""
from pylab import *

X= linspace( -2 ,2 ,40)
Y= linspace( -2 ,2 ,24)
X,Y= meshgrid(X, Y)

"""
Find the vector 'i' and 'j'
"""
u = X
v = -Y

"""
Plot the vector field
"""
Q = quiver(X,Y,u,v)

show()