#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:25:51 2019

@author: sebw
"""
# Citation:
# Wulfram Gerstner, Werner M. Kistler, Richard Naud, and Liam Paninski.
# Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition.
# Cambridge University Press, 2014.
# http://neuronaldynamics.epfl.ch

import numpy as np

def update(state_s0, weights):
    random_neuron_idx_list = np.random.permutation(len(state_s0))
    state_s1 = state_s0.copy()
    for i in range(len(random_neuron_idx_list)):
        rand_neuron_i = random_neuron_idx_list[i]
        h_i = np.dot(weights[:, rand_neuron_i], state_s1)
        s_i = np.sign(h_i)
        if s_i <= 0:
            s_i = 0
        state_s1[rand_neuron_i] = s_i
    return state_s1