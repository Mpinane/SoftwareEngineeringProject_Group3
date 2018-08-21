import unittest
import PrimeGenerator
import pandas as pd

def read_Cases():
         dataFrame=pd.read_csv('/home/lucky/Desktop/Software Engineering/Labs/Lab 2/Data/Cases.csv')
         input_X=dataFrame['INPUT_X']
         output_arrays_str=dataFrame['OUTPUT_ARRAY']
         output_n=dataFrame['OUTPUT_N']
         output_arrays=[]
         input_X=[int(i) for i in input_X]
         output_n=[int(i) for i in output_n]
         for i in range(len(output_arrays_str)):
             array=output_arrays_str[i]
             array=array[1:len(array)-1]
             int_array=array.split(',')
             int_array=[int(j) for j in int_array]
             output_arrays.append(int_array)
         return input_X,output_arrays,output_n
         
class TestGenerator(unittest.TestCase):
    
    def test_PrimeGenerator(self):
        output=read_Cases()
        X=output[0]
        array=output[1]
        n=output[2]
        for i in range(len(X)):
            result=PrimeGenerator.PrimeNumbers(X[i])
            self.assertEqual(result,(array[i],n[i]))
            
if __name__=='__main__':
    unittest.main()       

