# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:39:55 2022

@author: jaxfe
"""

import numpy 
import scipy 
import math
import time
import matplotlib as plt
from numpy import random
from numpy.random import Generator, PCG64
from numpy.random import Generator, MT19937
from time import perf_counter
from scipy.stats import chisquare


#Two pseudo-random number generators
rng1 = Generator(PCG64(seed = 456))
rng2 = Generator(MT19937(seed = 456))


#Create two strings of 10000 random numbers between (0,1) using identical seeds
#Time both processes to see which generator is quicker

t1_start = perf_counter()

rand1 = []
for i in range(10000):
    rand1.append(rng1.random())

t1_stop = perf_counter()

print("Time taken for PCG64:", t1_stop-t1_start)


t2_start = perf_counter()

rand2 = []
for i in range(10000):
    rand2.append(rng2.random())

t2_stop = perf_counter()

print("Time taken for Mersenne Twister:", t2_stop-t2_start)

#Run Chi square test on both sets of random numbers
 
rand1.sort()
rand2.sort()

def freq (N,M):
    string_length = len(N)
    bin_freq = [0]*M
    for k in range(0, string_length):
        for i in range(0,M):
            if N[k] > ((i)/M) and N[k] < ((i+1)/M) :
                bin_freq[i] = bin_freq[i] + 1
    return bin_freq

freq_PCG64 = freq(rand1,9000)    
freq_MT19937 = freq(rand2,9000)

chisquare(freq_PCG64)
chisquare(freq_MT19937)
