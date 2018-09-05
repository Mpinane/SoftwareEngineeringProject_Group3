# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:43:47 2018

@author: Mpinane
"""

import PrimeGenerator
import csv
import time

def calcTime(i):
    start = time.time()
    PrimeGenerator.PrimeNumbers(i)
    end = time.time()
    
    return end - start


inputs = []

inputFile =  open("performance_test_inputfile.txt",'r')
lines = inputFile.readlines()
inputFile.close
for i in lines:
    inputs.append(int(i.strip('\n')))

outputFile =  open("performance_test_outputfile.csv",'w+')
csvwriter = csv.writer(outputFile,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(["input"] + ["time"])
for i in inputs:
    csvwriter.writerow([i] + [calcTime(i)])
outputFile.close()

