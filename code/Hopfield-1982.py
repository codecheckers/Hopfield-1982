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
from matplotlib.figure import figaspect

from simulation import *

## number of neurons in the network
#N = 100
#
## number of stored states
#n = 5
#n = int(n)
#
# number of simulations
s = 100


# number of iterations
'''
ONE neuron is updated per iteration.

'''
x = 1000


'''
For reconstructing histograms in Fig. 2. Network initialised at a nominal memory state.
'''
Nerr1 = np.zeros(s)
Nerr2 = np.zeros(s)
Nerr3 = np.zeros(s)

for k1 in range(s):
    M = make_states(100, 5)
    T = make_weights(M)
    V = initialize(M, T, "nominal")
    V = evolve(M, T, V, x)
    
    state = M.shape[0]
    neuron = M.shape[1]
    
    error = min(np.sum(abs(M[0] - V)), (neuron - np.sum(abs(M[0] - V))))

    Nerr1[k1] = error

for k1 in range(s):
    M = make_states(100, 10)
    T = make_weights(M)
    V = initialize(M, T, "nominal")
    V = evolve(M, T, V, x)
    
    state = M.shape[0]
    neuron = M.shape[1]
    
    error = min(np.sum(abs(M[0] - V)), (neuron - np.sum(abs(M[0] - V))))

    Nerr2[k1] = error
    
for k1 in range(s):
    M = make_states(100, 15)
    T = make_weights(M)
    V = initialize(M, T, "nominal")
    V = evolve(M, T, V, x)
    
    state = M.shape[0]
    neuron = M.shape[1]
    
    error = min(np.sum(abs(M[0] - V)), (neuron - np.sum(abs(M[0] - V))))

    Nerr3[k1] = error
    
    
w, h = figaspect(4/5)
fig2, (ax1, ax2, ax3) = plt.subplots(3, sharex = True, figsize=(w,h))

ax1.hist(Nerr1, density = True, bins = range(0, 61))
ax1.text(0.83, 0.5, '$n=5$\n$N=100$', transform=ax1.transAxes, bbox=dict(fc="none"))
ax2.hist(Nerr2, density = True, bins = range(0, 61))
ax2.text(0.83, 0.5, '$n=10$\n$N=100$', transform=ax2.transAxes, bbox=dict(fc="none"))
ax3.hist(Nerr3, density = True, bins = range(0, 61))
ax3.text(0.83, 0.5, '$n=15$\n$N=100$', transform=ax3.transAxes, bbox=dict(fc="none"))
plt.xlabel("$N_{err}$")
ax2.set(ylabel = "Probability")


fig2.savefig("Fig 2.pdf")



'''
Network initialised at radom state. Output is the ratio of trials that ended at an assigned memory state with no error.
'''
#counter = 0
#for k1 in range(s):
#    M = make_states(N, n)
#    T = make_weights(M)
#    V = initialize(M, T, "random")
#    V = evolve(M, T, V, x)
#    
#    state = M.shape[0]
#    neuron = M.shape[1]
#
#    errorcount = np.zeros(state)
#    for k2 in range(state):
#        errorcount[k2] = np.sum(abs(M[k2] - V))
#    minimumerror = min(np.amin(errorcount), (neuron - np.amax(errorcount)))
#    
#    if minimumerror == 0:
#        counter += 1
#counter /= s
#print(counter)


