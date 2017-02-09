from math import sqrt

def primes(n):
    from math import sqrt

    A,B,C = [],[],[]

    for i in range(n+1):
        A.append(i) #Initialize A, from 0 to 2000000
        B.append(1) #Initialize B, containing all 1s from 0 to 2000000

    # Remove 0 and 1 from A

    if n == 0:
        return([])

    if n == 1:
        return([])
    
    A.reverse()
    A.pop()
    A.pop()
    A.reverse()

    B[0] = 0
    B[1] = 0

    root = sqrt(n) #Enough to check until root(i)
    
    for a in A:
        # Check until root(i)
        if a > root:
            break
        
        #  Remove all the multiples of A
        loopcount = n//a
        loopcount -= 1

        # Remove the number from the list
        for var in range(loopcount):
            B[(a*(var+2))] = 0

    for var in range(len(B)):
        if B[var] == 1:
            C.append(var)

    return(C)

def factors(Number):
    Root   = sqrt(Number)
    Root   = Root//1
    Primes = primes(200)
    Facts  = []
    
    for i in range(len(Primes)):
        Facts.append(0)
        
    for i in range(len(Primes)):
        Prime = Primes[i]
        while(Number%Prime==0):
            Number = Number/Prime
            Facts[i] += 1

            if Number == 1:
                return(Facts)

    return(Facts)

def factorcount(n):
    Number = n*(n+1)/2
    Facts  = factors(Number)
    Prod   = 1

    for i in range(len(Facts)):
        Prod *= (Facts[i]+1)

    return(Prod)

def main(n):    
    for i in range(40000):        
        
        FactorCount = factorcount(i+1)

        print(i+1)
        
        if FactorCount > n:
            return((i+2)*(i+1)/2)

    return(-1)

        
print(main(500))    
