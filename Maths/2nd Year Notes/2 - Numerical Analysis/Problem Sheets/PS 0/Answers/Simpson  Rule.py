import numpy as np
import matplotlib.pyplot as plt

def simps(f,a,b,n=50):
    '''
    Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.

    Examples
    --------
    >>> simps(lambda x : 3*x**2,0,1,10)
    1.0
    '''
    
    if a > b:
        print("Incorrect bounds")
        return None
    if n%2 != 0: # Ensure 'n' is even
        print("Invalid choice of n")
        return None
    else:
        h = (b-a)/n # need to cast 'n' as float in order to avoid integer division
    
        sum1 = 0
        for i in range(1, n//2 + 1):
            sum1 += f(a + (2*i - 1)*h)
        sum1 *= 4
    
        sum2 = 0
        for i in range(1, n//2): # range must be ints: range() integer 
            #end argument expected, got float.
            sum2 += f(a + 2*i*h)
        sum2 *= 2
    
        approx = ((b - a)/(3.0*n))*(f(a) + f(b) + sum1 + sum2)
        print("Height " + str(h))
        return approx
    
for x in range(1,7):
    approx = simps(lambda x: x**3-2*x, 0, 1, 4**x)
    error = (-0.75 - approx)
    
    print("Approximated answer " + str(x) + " is: " + str(approx))
    print("Error is: " + str(abs(error)))
