#! /usr/bin/env python

import math
import numpy as np

#################
# Random class
#################
# class that can generate random numbers
class Random:

    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)

        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()
# function returns random integer between 1 and 100
    def myrandint(self,min=1., max=100.):
        ran1 = self.rand()
        ran2 = self.rand()*100
        Inti = 100*ran1%ran2
        print (min, max , Inti)
        while Inti>max or Inti<min :
            ran1 = self.rand()
            ran2 = self.rand()
            #print (Inti)
        return int(Inti)

    def exponential(self,beta =0.05):
        if beta <=0.:
            beta = 1.
        temp_min = 1.
        temp_max = 40.
        #limiting my exponential function to generate the numbers in the range
        #fast version
        R = np.exp(-temp_max*beta) + (np.exp(-temp_min*beta)-np.exp(-temp_max*beta)) *self.rand()
        #print ("random is ",R)
        #limiting in range slow version
        temp = -math.log(R)/beta
        #print ("temperature is ",temp)
        """temp = -temp_max.
        while temp<-temp_min or temp>temp_max:
            R = self.rand()
            while R<=0:
                R = self.rand()
            temp = -math.log(R)/beta"""
        return temp


        #print ("temperature is ",temp)
        """temp = -temp_max.
        while temp<-temp_min or temp>temp_max:
            R = self.rand()
            while R<=0:
                R = self.rand()
            temp = -math.log(R)/beta"""
        return X



    def parabolic_dist(self,temp=30.,rate_min = 1. , rate_max = 20.):
        #room_temp = 30.
        low_temp = 0.0001
        high_temp= 200.
        if temp < low_temp:
            print("temperature is too low  \n changing the  value of a to  %f " % low_temp)
            temp = low_temp

        if temp > high_temp :
            print("temperature is too low  \n changing the  value of a to  %f " % high_temp )
            #temp = high_temp
        change_temp = temp #abs(temp-room_temp)
        Myrand = self.rand()
        scaler = (1./3.)*rate_min**3
        X= np.cbrt(3*(Myrand)/change_temp)
        #y_max = temp*rate_max**2
        #yrand = y_max *self.rand()


        """x = rate_min + (rate_max-rate_min)*self.rand()
        y_true = temp*x*x
        R = y_max/y_true
        newrand = self.rand()
        while newrand>R:
            newrand =self.rand()"""

        #R =  self.rand()
        #while R > prob:
        #    R = self.rand()


        while X<rate_min or X>rate_max:
            Myrand = self.rand()
            X= np.cbrt(3*(Myrand)/change_temp)
        #print (X)
        return X
