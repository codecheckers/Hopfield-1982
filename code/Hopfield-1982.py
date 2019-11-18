#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:14:33 2019

@author: sebw, nuest
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from matplotlib.figure import figaspect

from simulation import *

# number of neurons in the network
N = 100

# number of stored states
#n = 5
#n = 10
#n = 15

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
    M = make_states(N, 5)
    T = make_weights(M)
    V = initialize(M, T, "nominal")
    V = evolve(M, T, V, x)
    
    state = M.shape[0]
    neuron = M.shape[1]
    
    error = min(np.sum(abs(M[0] - V)), (neuron - np.sum(abs(M[0] - V))))

    Nerr1[k1] = error

for k1 in range(s):
    M = make_states(N, 10)
    T = make_weights(M)
    V = initialize(M, T, "nominal")
    V = evolve(M, T, V, x)
    
    state = M.shape[0]
    neuron = M.shape[1]
    
    error = min(np.sum(abs(M[0] - V)), (neuron - np.sum(abs(M[0] - V))))

    Nerr2[k1] = error
    
for k1 in range(s):
    M = make_states(N, 15)
    T = make_weights(M)
    V = initialize(M, T, "nominal")
    V = evolve(M, T, V, x)
    
    state = M.shape[0]
    neuron = M.shape[1]
    
    error = min(np.sum(abs(M[0] - V)), (neuron - np.sum(abs(M[0] - V))))

    Nerr3[k1] = error
    
    
w, h = figaspect(1/1)
fig2, (ax1, ax2, ax3) = plt.subplots(3, sharex = True, figsize=(w,h))

bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]

hist1, bins1 = np.histogram(Nerr1, density = True, bins = bins)
width = 0.7 * (bins[1] - bins[0])
ax1.bar(bins[:-1], hist1, align='center', width = width, color = 'white', edgecolor = 'black', hatch = "////////")
ax2.set_yticks([0.5, 1.0])
ax1.text(0.2, 0.5, '$n = 5$\n$N = 100$', transform = ax1.transAxes)

hist2, bins2 = np.histogram(Nerr2, density = True, bins = bins)
ax2.bar(bins[:-1], hist2, align='center', width = width, color = 'white', edgecolor = 'black', hatch = "////////")
ax2.set_yticks([0.2, 0.5])
ax2.text(0.2, 0.5, '$n = 10$\n$N = 100$', transform = ax2.transAxes)

hist3, bins3 = np.histogram(Nerr3, density = True, bins = bins)
ax3.bar(bins3[:-1], hist3, align='center', width = width, color = 'white', edgecolor = 'black', hatch = "////////")
ax3.set_xticks(bins[:-1])
ax3.set_yticks([0.1, 0.2])
ax3.set_xticklabels(["", "", "", "3", "", "", "6", "", "", "9", "        10-19", "20-29", "30-39", "40-49", ">49"])
ax3.text(0.2, 0.5, '$n = 15$\n$N = 100$', transform = ax3.transAxes)

plt.xlabel("$N_{err}$ = Number of Errors in State")
ax2.set(ylabel = "Probability")


fig2.savefig("Fig 2.pdf")
