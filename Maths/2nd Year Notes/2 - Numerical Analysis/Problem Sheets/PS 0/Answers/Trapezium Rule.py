import numpy as np
import matplotlib.pyplot as plt


def trapz(f,a,b,N=50):
    '''
    Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral \int_a^b f(x) dx by the sum:
    
    f(a + i*h)/2.0 + f(a + i*h)/2.0 =  f(a + i*h) 

    Parameters
    ----------
    f : function
        
    a , b : numbers
        Interval of integration [a,b]
    N : integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal length.

    Examples
    --------
    >>> trapz(np.sin,0,np.pi/2,1000)
    0.9999997943832332
    '''
    h = float(b - a) / N
    s = 0.0
    s += f(a)/2.0
    for i in range(1, N):
        s += f(a + i*h)
    s += f(b)/2.0
    print("h is: " + str(h))
    return s * h

for x in range(1,7):
    approx = trapz(lambda x: x**3-2*x, 0, 1, 4**x)
    error = (-0.75 - approx)
    
    print("Approximated answer " + str(x) + " is: " + str(approx))
    print("Error is: " + str(abs(error)))






