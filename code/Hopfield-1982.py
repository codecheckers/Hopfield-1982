#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:14:33 2019

@author: sebw
"""

import numpy as np
import matplotlib as plt
from update import *

# number of neurons in the network
N = 30

# number of stored states
n = 3
n = int(n)

# memory states (each row is a stored state)
M = np.zeros((n, N))

# state vector V 
V = np.zeros(n)

# weight matrix T
T = np.zeros((N, N))

# number of simulations
s = 100

# number of steps


# radomly generate memory states
for k in range(n):
    M[k] = np.random.randint(2, size = N)
    
# set weight matrix according to memory states
for k in range(n): # go through each memory state
    for i in range(N):
        for j in range(N):
            T[i, j] += (2 * M[k, i] - 1) * (2 * M[k, j] - 1)
T /= N
np.fill_diagonal(T, 0)

print(M)
#print(T)

# radom initial state of V
V = np.random.randint(2, size = N)

print(V)

for k in range(5):
    V = update(V, T)

print(V)

        
        