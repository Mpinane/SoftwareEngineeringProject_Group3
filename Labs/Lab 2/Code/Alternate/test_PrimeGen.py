import unittest 
import time
import sys
from PrimeGen import PrimeNumbers

class AlternativeTests(unittest.TestCase):
    def test_value(self):
        for i in range(X): #X same as Parameter passed to PrimeNumbers(X)
        #for i in range(len(PrimeNumbers(X)[0])):    
            if not self.assertTrue(isPrime([PrimeNumbers(X)[0]][i])):
                self.assertRaises(ValueError, PrimeNumbers(X)[0][i])
            
                
    def test_type(self):
        self.assertRaises(TypeError,PrimeNumbers,True)
        self.assertRaises(TypeError,PrimeNumbers,"This is a String")
        self.assertRaises(TypeError,PrimeNumbers,10 + 2j)
        self.assertRaises(TypeError,PrimeNumbers,[1,2,3,4,5])
        self.assertRaises(TypeError,PrimeNumbers,list(["a","b","c","d","e"]))
    
    def test_timePerformance(self):
        for i in range(1,1000000,10000):
            start_time = time.time()
            PrimeNumbers(i)
            end_time = time.time()
            
            if i >= 100000000:
                if end_time - start_time >= i*0.001
                    self.assertRaises(TimeoutError)
            
            elif i >= 10000000:
                if end_time - start_time >= i*0.001
                    self.assertRaises(TimeoutError)
            
            elif i >= 1000000:
                if end_time - start_time >= i*0.0001
                    self.assertRaises(TimeoutError)
            
            else:
                end_time - start_time >= i*0.00001
                self.assertRaises(TimeoutError)
                #self.assertRaises(TimeoutError,PrimeNumbers,i) 
