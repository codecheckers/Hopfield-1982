#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:25:51 2019

@author: sebw
"""

# Reference:
# Wulfram Gerstner, Werner M. Kistler, Richard Naud, and Liam Paninski.
# Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition.
# Cambridge University Press, 2014.
# http://neuronaldynamics.epfl.ch

import numpy as np

'''
Update the state of one randomly selected neuron according to update rule.
'''
def update(state_s0, weights):
    random_neuron = np.random.randint(len(state_s0))
    state_s1 = state_s0.copy()
    h_i = np.dot(weights[:, random_neuron], state_s1)
    s_i = np.sign(h_i)
    if s_i < 0:
        s_i = 0
    state_s1[random_neuron] = s_i
    
#    random_neuron_idx_list = np.random.permutation(len(state_s0))
#    state_s1 = state_s0.copy()
#    for i in range(len(random_neuron_idx_list)):
#        rand_neuron_i = random_neuron_idx_list[i]
#        h_i = np.dot(weights[:, rand_neuron_i], state_s1)
#        s_i = np.sign(h_i)
#        if s_i < 0:
#            s_i = 0
#        elif s_i == 0:
#            s_i = 1
#        state_s1[rand_neuron_i] = s_i
    
    return state_s1

def make_states(neuron, state):
    # memory states (each row is a memory state)
    M = np.zeros((state, neuron))
    
    # radomly generate memory states
    for k in range(state):
        M[k] = np.random.randint(2, size = neuron)
    return M

def make_weights(M):
    state = M.shape[0]
    neuron = M.shape[1]
    
    # weight matrix T
    T = np.zeros((neuron, neuron))
            
    # set weight matrix according to memory states
    for k in range(state): # go through each memory state
        for i in range(neuron):
            for j in range(neuron):
                T[i, j] += (2 * M[k, i] - 1) * (2 * M[k, j] - 1)
    T /= neuron
    np.fill_diagonal(T, 0)
    
    return T
    
def initialize(M, T, mode):
    state = M.shape[0]
    neuron = M.shape[1]
    
    # state vector V 
    V = np.zeros(neuron)
    
    if mode == "random":
        # radom initial state of V
        V = np.random.randint(2, size = neuron)
    elif mode == "nominal":
        # initialise at a nominal memory state
        V = M[0]
    
    return V

def evolve(M, T, V, x):
    state = M.shape[0]
    neuron = M.shape[1]
    
    # network evolve    
    errorcount = np.zeros(state)
    i = 0
    errorhistory = []
    while True:
        i += 1
        V1 = update(V, T)
        
#        if radominit:
#            for k in range(state):
#                errorcount[k] = np.sum(abs(M[k] - V1))
#            minimumerror = min(np.amin(errorcount), (neuron - np.amax(errorcount)))
#            
#        else:
#            error = np.sum(abs(M[0] - V1))
#            errorhistory.append(error)
        
        V = V1
        if i == x:
            break
    return V
