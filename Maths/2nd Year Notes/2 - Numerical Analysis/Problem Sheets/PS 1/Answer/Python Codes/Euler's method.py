import numpy as np
import matplotlib.pyplot as plt

'''
Euler's method.py:

The classical Euler's method. 

The program does the following:
- Generates an array of values from the function
- Generates an array of approximated values from Euler's 
- Plot the values of the two array
- Compares the two arrays and generates an additional array - the error array

for the following differential equation:
    dy/dx = x+y where y(0) = 2
'''
def Euler (f, x, y0):
    '''
    Finds the true values of a given function

    Parameters
    ----------
    f : function
    x : array of x-axis values
    y0 : Initial conditions

    Returns
    -------
    array : estimated values of a function

    Examples
    --------
    >>> GenerateTrue(lambda x : 3*x**2,x)
    '''
    y_approx = np.zeros(len(x))  # Declare the array to be returned
    y_approx[0] = y0 # Insert initial values
    for n in range(0,len(x)-1):
        y_approx[n+1] = y_approx[n] + f(y_approx[n],x[n])*(x[n+1] - x[n])
    return y_approx
    
    
    

y0 = 2
h = 0.02
x_final = 1
N = round((x_final-0)/h)

x = np.linspace(0,x_final,N) # Generate the array of x-values 
y_true = np.zeros(len(x)) # Generate the array of true y-values 
y_approx = np.zeros(len(x)) # Generate the array of estimated y-values

y_approx = Euler(lambda y, x: x+y, x, y0)

for n in range(0,len(x)): # Find array of true values
    y_true[n] = 3*np.exp(x[n])-x[n]-1 

plt.plot(x,y_true,'b.-',x,y_approx,'r-')
plt.legend(['True', 'Euler'])
plt.axis([0,1,0,8])
plt.grid(True)
plt.title("True vs Euler")
plt.show()
