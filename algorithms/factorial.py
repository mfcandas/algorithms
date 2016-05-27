# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:23:51 2016

@author: mcandas
"""

import numpy as np

path = 3267
demand = 1000

num1= (np.math.factorial(path+demand))

num2= ((np.math.factorial(path)*np.math.factorial(demand)))


num3= (num1//num2)


i = 1
pow1 = 0
while (i < num1):
    i*=10
    pow1 += 1
    
print (pow1)


i = 1
pow2 = 0
while (i < num2):
    i*=10
    pow2 += 1
    
print (pow2)

print (pow1-pow2)
    

i = 1
pow3 = 0
while (i < num3):
    i*=10
    pow3 += 1
    
print (pow3)

print (math.log(num3,10))