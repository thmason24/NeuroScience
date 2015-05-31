# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:57:25 2015

@author: Tim
"""

import pickle
import matplotlib.pyplot as plt
import numpy as np
import pylab as P

with open('tuning.pickle', 'rb') as f:
    data = pickle.load(f)
    

stimVec=data['stim']
mean=data['neuron4'].mean(0)
print(mean.shape)

#plt.plot(stimVec,mean)
neuron=4
stim=3

mean=data['neuron1'].mean(0)
dir1=stimVec[mean.argmax()]
max1=mean.max()
print(dir1 ,  max1)


mean=data['neuron2'].mean(0)
dir2=stimVec[mean.argmax()]
max2=mean.max()
print(dir2, max2)


mean=data['neuron3'].mean(0)
dir3=stimVec[mean.argmax()]
max3=mean.max()
print(dir3, max3)

mean=data['neuron4'].mean(0)
dir4=stimVec[mean.argmax()]
max4=mean.max()
print(dir4, max4)


#print(P.hist(data['neuron' + str(neuron)][:,stim]))
#plt.figure()
#plt.plot(data['neuron' + str(neuron)][:,stim])

#for stim in range(1,len(data['stim'])):
    #print(data['neuron' + str(neuron)][:,stim].mean())
    #print(data['neuron' + str(neuron)][:,stim].var())
#    print(data['neuron' + str(neuron)][:,stim].mean()/data['neuron' + str(neuron)][:,stim].var())


with open('pop_coding.pickle', 'rb') as f:
    data = pickle.load(f)

print(data['r1'])
print()    
print(np.arccos(data['r1'].mean()/max1)*(180/np.pi) , data['c1'])
print(np.arccos(data['r2'].mean()/max2)*(180/np.pi) , data['c2'])
print(data['r3'].mean()/max3 , data['c3'])
print(data['r4'].mean()/max4 , data['c4'])


