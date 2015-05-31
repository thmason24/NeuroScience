# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:57:25 2015

@author: Tim
"""

import pickle
import matplotlib.pyplot as plt
import numpy as np
import pylab as P

with open('pop_coding.pickle', 'rb') as f:
    data = pickle.load(f)
    
print(data.keys())
#plt.plot(data['stim'])
#plt.plot(data['neuron4'])



#mean=data['neuron4'].mean(0)
#print(mean.shape)
#
##plt.plot(data['stim'],mean)
#neuron=4
#stim=3
##print(P.hist(data['neuron' + str(neuron)][:,stim]))
##plt.figure()
##plt.plot(data['neuron' + str(neuron)][:,stim])
#
#for stim in range(1,len(data['stim'])):
#    #print(data['neuron' + str(neuron)][:,stim].mean())
#    #print(data['neuron' + str(neuron)][:,stim].var())
#    print(data['neuron' + str(neuron)][:,stim].mean()/data['neuron' + str(neuron)][:,stim].var())
#
