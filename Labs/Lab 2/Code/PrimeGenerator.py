def PrimeNumbers(X):
    primes=[]
    counter=2
    while counter<=X:
        isPrime=True
        for i in range(2,X):
            if (counter % i)==0 and (counter!=i):
                isPrime=False
                break
        if isPrime:
            primes.append(counter)
        counter=counter+1
    N=len(primes)
    return primes,N

PrimeNumbers(19)   