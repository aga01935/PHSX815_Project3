#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
from python.Random import Random
# Electricity Analysis Main Function
if __name__ == "__main__":
    # if user do not provide any arguments  or provide -h then print this option
    if '-h' in sys.argv or '--help' in sys.argv :
        print ("Usage: %s [-seed number] [options]" % sys.argv[0] )
        print ("options:")
        print ("-seed <number >        provide any four digit seed for random number, default is 5555" )
        print ("-npar <integer>        number of true parameter to be generated, default is 100")
        print ("-Nmes <number>         number of measurements to make, default is 1")
        print ("-Nexp <number>         number of experiment to perform, default is 1")
        print ("-output <string>       name of output file to produce, default is 1")
        #print ("-temp <number>         outside temperature , default is 30 celsious")
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default rate parameter for electric device normal use  (cookies per day)
    npar = 100

    #default measurement
    Nmeas = 1

    # default number of experiments
    Nexp = 1

    #Temperature in celcious
    temp = 30.

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-npar' in sys.argv:
        p = sys.argv.index('-npar')
        ptemp = sys.argv[p+1]
        npar = int(ptemp)
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
    #if '-temp' in sys.argv:
    #    p = sys.argv.index('-temp')
    #    tp = float(sys.argv[p+1])
    #    temp = tp
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = Random(seed)
    if doOutputFile:


        for g in range(1,npar):

            outname_temp = "temp"+OutputFileName
            outfile = open(str(g)+OutputFileName, 'w')
            outfile_temp = open(str(g)+outname_temp,'w')
            temp = random.exponential(0.02)/10.
            #temp = g/10.
            print (temp)
            #temp = 40
            for e in range(0,Nexp):
                for t in range(0,Nmeas):
                    #temp = random.exponintial(0.02)
                    #outfile.write(str(random.parabolic_dist(temp,0.,100.))+" ")
                    #print(random.exponential(temp,0.,10.))
                    outfile.write(str(random.parabolic_dist(temp,1.,10.))+" ")
                    #print(random.exponential2(temp,0.,10.))

                outfile_temp.write(str(temp)+" ")
                outfile_temp.write(" \n")
                outfile.write(" \n")
        outfile.close()
