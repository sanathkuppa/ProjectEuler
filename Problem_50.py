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

def Primes(n):
    B = PrimeArray(n)
    C = []
    for var in range(len(B)):
        if B[var] == 1:
            C.append(var)

    return(C)

Limit = 1000000
Count  = -1
Max    = -1
Prime  = -1
Primes = Primes(Limit)
Array  = PrimeArray(Limit)

for i in range(len(Primes)):
    Count = 1
    Sum   = Primes[i]

    for j in range(i+1, len(Primes)):
        Sum   += Primes[j]
        Count += 1

        if Sum > len(Array)-1:
            break

#        print(Sum)
        if Array[Sum]: #if the sum is a prime
##            print(Count)
##            print(Max)
            if Count > Max:
                Prime = Sum
                Max   = Count
                print(Prime)
                print(Max)
                
            
    
