#To run on Linux: python -m unittest test_PrimeGen
#Shows number of test cases (test functions) the PrimeNumbers functions passed
#All the passed cases are possible handled inputs and run time scenarios
import unittest 
import time
import sys
from PrimeGen import PrimeNumbers
from PrimeGen import PrimeNumberCheck
import random

class AlternativeTests(unittest.TestCase):
                
    def test_type(self):
        self.assertRaises(TypeError,PrimeNumbers,True)
        self.assertRaises(TypeError,PrimeNumbers,"This is a String")
        self.assertRaises(TypeError,PrimeNumbers,10 + 2j)
        self.assertRaises(TypeError,PrimeNumbers,[1,2,3,4,5])
        self.assertRaises(TypeError,PrimeNumbers,list(["a","b","c","d","e"]))
    
