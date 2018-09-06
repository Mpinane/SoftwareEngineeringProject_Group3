import unittest 
import sys

def PrimeNumbers(X):    
    if type(X) == int and X < 2:
        raise ValueError("Integer has to be equal to or greater than 2.")
    elif type(X) == list :
        raise TypeError("Input can not be a list or array.")
    elif type(X) == bool:
        raise TypeError("Input can not be boolean.")
    elif type(X) == complex:
        raise TypeError("Input can not be a complex number.")
    elif len(str(X)) >= 10:
        raise ValueError("Input too Large.")
    elif type(X) not in [int]:
        raise TypeError("Please Enter a Postive Integer.")
    
    primes=[]
    counter=2
    while counter<=X and counter < sys.maxsize+1:
        isPrime=True
        for i in range(2,X):
            if (counter % i)==0 and (counter!=i):
                isPrime=False
                break
        if isPrime and PrimeNumberCheck(counter):
            primes.append(counter)
        counter=counter+1
    N=len(primes)
    return primes,N

def PrimeNumberCheck(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 
