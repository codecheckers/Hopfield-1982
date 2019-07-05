#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:14:33 2019

@author: sebw
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from simulation import *

# number of neurons in the network
N = 30

# number of stored states
n = 5
n = int(n)



# number of simulations
s = 100

# number of iterations
x = 1000


'''
For reconstructing histograms in Fig. 2. Network initialised at a memory state.
'''
#Nerr = np.zeros(s)
#for k in range(s):
#    Nerr[k] = runsim(N, n, x)
#
#plt.hist(Nerr, density = True, bins = range(0, N + 1))
#plt.show


'''
Network initialised at radom state. Output is the ratio of trials that ended at an assigned memory/
'''
counter = 0
for k in range(s):
    if runsim(N, n, x, True) == 0:
        counter += 1
counter /= s
print(counter)


