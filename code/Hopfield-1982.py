#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:14:33 2019

@author: sebw
"""

import numpy as np
import matplotlib as plt

#number of neurons in the network
N = 100

#number of stored states
n = 0.15 * N

#memory states (each row is a stored state)
M = np.zeros(n, N)

#state vector V 
V = np.zeros(n)

#weight matrix T
T = np.zeros(n, n)

#number of simulations
s = 100

#radomly generate memory states
for k in range(n):
    M[k] = np.random.randint(2, size = N)
    
#set weight matrix according to memory states

        