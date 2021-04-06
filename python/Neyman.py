import numpy as np
import math
import matplotlib.pyplot as plt
from random import random

Nmeas = 100
Nexp = 1000
pram_experiment =  0.
beta_true_list = []
beta_best_list =[]


for i in range (1,100):
    beta_true = float(i)/10.
    for j in range(0,Nexp):
        beta_best = 0.
        for k in range(0,Nmeas):

            x = np.random.poisson(beta_true,1)
            beta_best = beta_best + x # np.log(float(x))

        beta_best = float(beta_best)/float(Nmeas)
        beta_best_list.append(float(beta_best))
        beta_true_list.append(float(beta_true))


#print (beta_true_list)
#print (beta_best_list)
#print
plt.figure()

plt.hist2d(beta_true_list,beta_best_list, bins = 100)
ax = plt.axes()
ax.set_facecolor('white')
plt.xlabel('True Value of ' + r'$\lambda$')
plt.ylabel('Measured Value of' + r'$\lambda$')
plt.title('Neyman Construction (Poission Distribution) ')
plt.show()
