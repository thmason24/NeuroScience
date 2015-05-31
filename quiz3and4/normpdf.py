# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:42:34 2015

@author: Tim
"""

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = norm.stats(moments='mvsk')
print(kurt)
mean = 5
std  = 3
#x = np.linspace(norm.ppf(0.01,loc=mean,scale=std),norm.ppf(0.99,loc=mean,scale=std), 100)
#ax.plot(x, norm.pdf(x,loc=5,scale=std),'r-', lw=5, alpha=0.6, label='norm pdf')


x=np.linspace(3,9)
R1=norm.pdf(x,loc=5,scale=0.5)
R2=norm.pdf(x,loc=7,scale=1)
ax.plot(x, 2*R1, x, R2,'r-', lw=5, alpha=0.6, label='norm pdf')
