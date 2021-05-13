#! /usr/bin/env python

# imports of external packages to use in our code
import sys
#import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.colors import LogNorm
import ROOT as rt

#
from scipy.optimize import curve_fit
sys.path.append(".")
from Random import Random
from MySort import MySort
plt.rcParams['axes.facecolor'] = 'white'
if __name__ == "__main__":
    def parabola(par,x):
        value = (par[0])*x*x
        return value
    def exponential(par,x):
        val = (1./float(par[0])) * math.exp(-float(x)/float(par[0]))
    npar = 1
    Nexp = 1
    Nmeas = 1
    seed = 5555
    print (sys.argv[0])

    if '-npar' in sys.argv:
        p = sys.argv.index('-npar')
        npar = int(sys.argv[p+1])
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nmeas = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne


    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("options:")
        print ("-seed <number >        provide any four digit seed for random number, default is 5555" )
        print ("-npar <integer>        number of true parameter to be generated, default is 100")
        print ("-Nmes <number>         number of measurements to make, default is 1")
        print ("-Nexp <number>         number of experiment to perform, default is 1")
        print ("-output <string>       name of output file to produce, default is 1")

        print
        sys.exit(1)
    Meas_Param = []
    Data = []
    sorter = MySort()

# simulating the experiment:
    true_temp =[]
    calculated_temp =[]
    diff_temp = []
    random = Random(seed)
    print (npar,Nmeas,Nexp,seed)
    for g in range(1,npar+1):

        #temp = random.exponential(0.02)/10.
        temp = float(g)/100.

        #print (temp)

        for e in range(0,Nexp):
            #exptemp = []
            dataval =[]
            #ydata =[]
            #xdata =[]
            for t in range(0,Nmeas):
                val = random.parabolic_dist(temp,1.,10.)
                #np.random.exponential(temp)
                #random.parabolic_dist(temp,1.,10.)
                #true_temp.append(temp)
                dataval.append(val)
                #exptemp.append(temp)

            y,x = np.histogram(dataval,density = True,bins =100)
            """
            plt.figure()
            plt.hist(dataval,alpha =1, density =True)
            plt.title("Simulated Distribution for "+ str(Nmeas) + " Measurements/Experiments")
            plt.xlabel("Time between the measurements")
            plt.ylabel("Probability")
            plt.show()

            """


            ydata = list(y)
            xdata =list(x[:-1])

            #print (xdata[0],ydata[0])
            #c_temp, pcov = curve_fit(parabola, xdata[:-1], ydata, p0=1)

            #c_temp, pcov = curve_fit(exponential, xdata[:-1], ydata, p0=1.)
            #c_temp = round(c_temp[0],4)

            #calc_y =[]
            calc_temp =[]
            #x_plotter = np.arange(1,10,0.001)
            #print ("length of xdata is ",len(xdata))

            for i in range(0,len(xdata)):
                tcal = float(ydata[i])/float((xdata[i]*xdata[i]))
                calc_temp.append(tcal)
            #    calc_y.append(tcal/100.)

            #c_temp = sum(calc_temp)/len(calc_temp)
            yt,xt = np.histogram(calc_temp,bins = 20,density = True)
            #print (xt)
            #print (yt)
            xt = list(xt[:-1])
            yt = list(yt)
            #xt = xt.sort()
            #print (xt)
            #print(yt)



            #c_temp2 = max(calc_temp, key=calc_temp.count)

            it = 0
            for it in range(len(yt)):


                if (np.isclose(yt[it], max(yt),atol = 0.001)):
                    #print (yt[it], max(yt), xt[it],it)
                    c_temp = xt[it]
            #print ("calculated temp ", c_temp, c_temp2)
            """plt.figure()
            plt.hist(calc_temp,bins = 20, density = True )
            plt.title("Calculate Temperature "+ str(Nexp)+ " Experiments/Paramter")
            plt.axvline(c_temp, label = "Maximum Likelihood", color = "r")
            plt.xlabel("Measured Temperature")
            plt.ylabel("Likelihood")
            plt.legend()
            plt.show()"""
            #plt.scatter(x_plotter,calc_y,color = "g", alpha =0.2)
            #print(calc_t)
            #plt.figure()
            #plt.scatter(xdata,ydata,color ="r")
            #plt.figure()
            #plt.hist(dataval,alpha =0.3,density = True)
            #plt.show()

            calculated_temp.append(c_temp)
            true_temp.append(temp)
            diff_temp.append((temp-c_temp))
            #print (temp, c_temp[0],(temp-c_temp[0]))
    #print(true_temp)
    #print (calculated_temp)
    #plt.figure()
    #print (max(calculated_temp),min(calculated_temp))
    #scale = (max(true_temp)-min(true_temp))/(max(calculated_temp)-min(calculated_temp))
    #calculated_temp = [x*scale for x in calculated_temp]

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
