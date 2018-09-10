# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:43:47 2018

@author: Mpinane
"""

import PrimeGenerator
import time
import matplotlib.pyplot as plt

def calcTime(i):
    start = time.time()
    PrimeGenerator.PrimeNumbers(i)
    end = time.time()
    
    return end - start


inputs = []
outputs = []

inputFile =  open("/home/lucky/SoftwareEngineeringProject_Group3/Labs/Lab 2/Data/performance_test_inputfile.txt",'r')
lines = inputFile.readlines()
inputFile.close

for i in lines:
    inputs.append(int(i.strip('\n')))

for i in inputs:
    sum = 0;
    for j in range(1000):
        sum = sum + calcTime(i)
    avg = sum/100
    outputs.append(avg)

plt.figure(figsize=(15,10), dpi=100)
plt.plot(inputs, outputs)
plt.xlabel('input')
plt.ylabel('time (sec)')
plt.show()
