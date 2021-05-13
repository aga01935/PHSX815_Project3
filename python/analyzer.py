import sys
#import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.colors import LogNorm
import ROOT as rt
InputFile0 = "file.txt"
InputFile1 = "tfile.txt"
Nexp = 10
Nmeas = 100
npar = 100

true_temp =[]
calculated_temp =[]
diff_temp = []
with open(InputFile0) as ifile,open(InputFile1) as ifile2:
    for line in ifile:
            lineVals = line.split()
            for t in lineVals:
                calculated_temp.append(float(t))

    for line in ifile2:
            lineVals = line.split()
            for t in lineVals:
                true_temp.append(float(t))
for i in range (len(calculated_temp)):
    diff_temp.append(true_temp[i]-calculated_temp[i])
h = plt.hist2d(true_temp,calculated_temp,bins = 10,norm = LogNorm())
plt.colorbar(h[3])
#plt.figure()
plt.xlabel("True Temperature")
plt.ylabel("Measured Temperature")
plt.title("Neyman Construction for "+ str(Nexp) + " Experiments/Parameter")
plt.show()
#n,xbin, patches = plt.hist(slice_diff,density =True ,bins =20)
#
sigmalist =[]
print (len(diff_temp))
for iterate in range(0,npar):
    Nslicelow = iterate*Nexp
    NsliceHigh = (iterate+1)*Nexp

    slice_diff = diff_temp[Nslicelow:NsliceHigh]

    n,xbin,_ = plt.hist(slice_diff,density =True ,bins =20)

    mu,sigma = norm.fit(slice_diff)
    y = norm.pdf( xbin, mu, sigma)
    plt.plot(xbin, y, 'r--',  linewidth=2)
    #plt.show()
    sigmalist.append(sigma)
    print(Nslicelow,NsliceHigh, sigma)
#print (sigmalist)
rt.gStyle.SetOptStat(0)
hist = rt.TH1D("histo", "Error in Parameter Estimation "+ str(Nexp)+ " Experiment Per Parameters",npar,min(true_temp),max(true_temp))
for int in range(1,npar+1):
    true_temp = float(int)/100.
    hist.Fill(true_temp)
    print(true_temp)
    hist.SetBinError(int-1,sigmalist[int-1])
    print(sigmalist[int-1])
canvas = rt.TCanvas("canvas","",600,600)
canvas.cd()
hist.Draw("e")
canvas.SaveAs("result.pdf")
