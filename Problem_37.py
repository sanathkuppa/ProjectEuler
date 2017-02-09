from math import sqrt

def PrimeArray(n):
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
            
    return(B)

def PrimeNo(n):
    C     = []
    Array = PrimeArray(n)
    for var in range(len(Array)):
        if Array[var] == 1:
            C.append(var)

    return(C)

def Smaller(n):
    Array = []
    Array.append(n)
    
    Temp  = n
    while Temp > 9:
        Temp = Temp//10
        Array.append(Temp)

    Temp  = n
    p     = 1
    while n//(10**p) != 0:
        Array.append(n%(10**p))
        p +=1

    return(Array)

Sum    = 0
Range  = 1000000
Primes = PrimeNo(Range)
Array  = PrimeArray(Range)

for i in Primes:
    smaller = Smaller(i)
    Req     = 1

    if i < 10:
        Req  = 0
    
    for j in smaller:
        Req *= Array[j]

    if Req == 1:
        print(i)
        Sum += i

print(Sum)

