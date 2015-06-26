# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:44:04 2015

@author: Tim
"""
import matplotlib.pyplot as mp
import pickle
import numpy as np
with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)
    
Input = data['c10p1']
Input[:,0]= Input[:,0] - Input[:,0].mean()
Input[:,1]= Input[:,1] - Input[:,1].mean()
#

#Input[:,0]= Input[:,0] 
#Input[:,1]= Input[:,1] 
#
#print(Input)

mp.scatter(Input[:,0],Input[:,1])

nu=1
alpha=1
dt=0.01
numSteps=100000

count=0
w = np.random.rand(2)
for i in range(numSteps):
    
    u = Input[count,:]
    v = np.dot(u,w)
    
    w = w + dt*nu*(v*u - alpha * v**2 * w)
    #w = w + dt*nu*(v*u)
        
            
    count += 1
    if count >= len(Input):
        count = 0
print('w vector')
print(w)

mp.scatter(w[0],w[1],color='r')
mp.scatter(0.71033657,  0.70386217,color='g')
mp.scatter(-0.70386217,  0.71033657,color='g')

cor = np.dot(Input.T,Input)/len(Input)
cov = np.cov(Input.T)
print('Eigen of cor')
print(np.linalg.eig(cor))
print('Eighern of cov')
print(np.linalg.eig(cov))

print()
print(cov)
print(cor)