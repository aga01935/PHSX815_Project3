import scipy as sp
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


#define a function here
def myfunc(x):
    return 2*x*x*x*x-6*x*x*x+8


x0 = np.arange(1,3.5,.01)


min = minimize(myfunc,1)


print ("Minimum of the function is : ","(",min.x[0],min.fun,")" )
plt.figure()
plt.plot(x0,myfunc(x0),"r",label ="Function")
plt.plot(min.x[0],min.fun,"bo",label = "Minimum of Function")
plt.title("Function minimization using Scipy")
plt.xlabel("x"+r"$\rightarrow$")
plt.ylabel("f(x)"+r"$\rightarrow$")
plt.legend()

plt.show()
