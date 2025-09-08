# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:49:37 2024

@author: yashd
"""

import numpy as np
import matplotlib.pyplot as plt

#Traget value (true value )
true_value= 50

#Simulate data
#1. Accurate and Precise (close to true value and tightly grouped )
'''
Loc = true_value (true_value = 50): The values will be
centerd around the true value(50)
scale=1: The standard deviation (spread) is small
meaning the values will be tightly grouped around the true value 
This implies high precision 
The mesurments will vary only a little from  the value,
so they'll be both accurate (close to 50) and
precise (close to each other)

'''
accurate_precise = np.random.normal(loc=true_value,scale=1,size=10)

#2 Accurate bur not precise (close to true value but spread out)
accurate_not_precise = np.random.normal(loc=true_value, scale=10,size=10)

'''
The toe lines of code you've highlighted may look similar,
but they differ in one important aspects: the value of scale,
which controls the spread of the generated values around the true value (loc)

'''
#3 Precise but Not Accurate (far from true value tighly grouped )
precise_not_accurate = np.random.normal(loc=70,scale=1,size=10)

#4 Neither Accurate nor Precise (far from tyrue value and spread out)
not_accurate_not_precise = np.random.normal(loc=70,scale=10,size=10)

#Ploting the results
plt.figure(figsize=(10,6))

#Plot 1 : Accurate and Precise 
plt.scatter(accurate_precise, [1]*10,color='green',label='Accurate and Precise')

#Plot 2 : Accurate but not Precise
plt.scatter(accurate_not_precise, [2]*10,color='blue',label='Accuaret but not Precise')

#plot 3 : Precise but not Accurate
plt.scatter (precise_not_accurate, [3]*10 , color='orange')

#Plot 4 : Neither Accurate nor Precise

plt.scatter(not_accurate_not_precise, [4]*10,color='red',label='Neither Accurate nor Precise')

#Adding target line
plt.axvline (true_value,color='black',linestyle='--',label='True Value')

#Labels and legend
plt.yticks([1,2,3,4],['Accurate and Precise','Accurate but not Precise','Precise but not Accurate','Neither Accuaret nor Precise '])
plt.xlabel('Measurment Value')
plt.legend()
plt.title('Accurate and Precise Demonstartion ')










