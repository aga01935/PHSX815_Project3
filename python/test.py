import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integ


x = np.linspace(0,100,1000)

y =list(np.exp(x))

print (x)
plt.figure()
plt.hist(x,density = True)
plt.show()
