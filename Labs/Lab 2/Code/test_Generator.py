import PrimeGenerator
import pandas as pd
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
string_code='-402'
def read_Cases():
         dataFrame=pd.read_csv('/home/lucky/SoftwareEngineeringProject_Group3/Labs/Lab 2/Data/Cases.csv')
         input_X=dataFrame['INPUT_X']
         output_arrays_str=dataFrame['OUTPUT_ARRAY']
         output_n=dataFrame['OUTPUT_N']
         output_arrays=[]
         
         for i in range(len(input_X)):
             if input_X[i]==string_code:
                 input_X[i]='-101'
         a = pd.to_numeric(dataFrame.INPUT_X, errors='coerce')
         ind=a.isna()
         input_X[ind]=string_code
         input_X=[int(i) for i in input_X]
         output_n=[int(i) for i in output_n]
         
         for i in range(len(output_arrays_str)):
             if len(output_arrays_str[i])!=2:
                 array=output_arrays_str[i]
                 array=array[1:len(array)-1]
                 int_array=array.split(',')
                 int_array=[int(j) for j in int_array]
                 output_arrays.append(int_array)
             else:
                 int_array=[]
                 output_arrays.append(int_array)
         return input_X,output_arrays,output_n
     
output=read_Cases()
X=output[0]
array=output[1]
n=output[2]     

def test(did_pass,i):
    if did_pass:
        if (X[i]>=2):
            msg="Case #{}(POSITIVE INTERGER INPUT): SUCCESSFULLY PASSED...  FOR INPUT: {} , RETURNED ARRAY IS {}".format(i+1,X[i],array[i])
        elif(X[i]<0 and X[i]!=int(string_code)):
            msg="Case #{}(NEGATIVE INTERGER INPUT): SUCCESSFULLY PASSED... FOR INPUT: NEGATIVE , RETURNED X IS EMPTY".format(i+1,X[i])
        elif(X[i]==0):
            msg="Case #{}(INPUT 0): SUCCESSFULLY PASSED... FOR INPUT: {} , RETURNED X IS EMPTY".format(i+1,X[i])
        elif(X[i]==1):
            msg="Case #{}(INPUT 1): SUCCESSFULLY PASSED... FOR INPUT: {} , RETURNED X IS EMPTY".format(i+1,X[i])
        elif(X[i]==int(string_code)):
            msg="Case #{}(STRING INPUT): SUCCESSFULLY PASSED... FOR INPUT: STRING , RETURNED X IS EMPTY".format(i+1,X[i],array[i])
    else:
        
        if (X[i]>=2):
            msg="Case #{}(POSITIVE INTERGER INPUT): FAILED...  FOR INPUT: {} , ONE OF THE OUTPUTS IS WRONG!".format(i+1,X[i])
        elif(X[i]<0 and X[i]!=int(string_code)):
            msg="Case #{}(NEGATIVE INTERGER INPUT): FAILED... FOR INPUT: NEGATIVE , ONE OF THE OUTPUTS IS WRONG!".format(i+1,X[i])
        elif(X[i]==0):
            msg="Case #{}(INPUT 0): FAILED... FOR INPUT: {} , ONE OF THE OUTPUTS IS WRONG!".format(i+1,X[i])
        elif(X[i]==1):
            msg="Case #{}(INPUT 1): FAILED... FOR INPUT: {} , ONE OF THE OUTPUTS IS WRONG!".format(i+1,X[i])
        elif(X[i]==int(string_code)):
            msg="Case #{}(STRING INPUT): FAILED... FOR INPUT: STRING , ONE OF THE OUTPUTS IS WRONG!".format(i+1,X[i])
    print(msg)

def test_suite():
    print("RUNNING TESTS...")
    for i in range(len(X)):
        test((PrimeGenerator.PrimeNumbers(X[i])==(array[i],n[i])),i)
        
test_suite()      
