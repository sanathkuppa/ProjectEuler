# Current Algo:
# 1. Generate the list of all the primes below n (fast)
# 2. Get the list of all the prime factors for all the numbers below n (fast)
# 3. Then compute the list of relative primes using n(AUBUC) = n(A) + ... - n(ANB) + n(ANBNC)... (slow)
# 4. Then check for the palindrome thing and compute ratios (fast)

from math import sqrt
from itertools import combinations
import numpy
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

def Factors(n):
    Primes  = primes(n)
    print("getting primes done")
    Factors = []
    
    for i in range(n+1):
        Factors.append([])
        
    for i in Primes:
        loopcount = n//i
        for j in range(loopcount):
            Factors[i*(j+1)].append(i)
    
    return(Factors)

def Phi(n,Array):
    # This seems to be the bottleneck. Can we think of a more efficient way?
    
    Sum = 0
    for i in range(1,len(Array)+1):
        Comb = combinations(Array,i)
        for j in Comb:
            List = list(j)
            Prod = numpy.prod(list(j))
            Sum = Sum + ((-1)**(len(j)-1))*n/Prod
    return(int(n-Sum))

def Output(n):
    Fact    = Factors(n)
    print("getting factors done")
    Candid  = [] 
    
    for i in range(2,n+1):
        Val  = Phi(i,Fact[i])
        Str1 = "".join(sorted(str(i)))
        Str2 = "".join(sorted(str(Val)))
        if(Str1==Str2):
            Candid.append([i,Val])
    return(Candid)        

def Answer(n):
    Candid = Output(n)
    Fact   = Factors(n)
    Test   = []
    print("getting candidates done")
    Min    = 100
    Fin    = 0
    for i in Candid:
        Val = i[0]/i[1]
        if Val < Min:
            Min = Val
            Fin = i[0]
            Test.append(len(Fact[i[0]]))
        
    print(Test)
    return(Fin)

print(Answer(10000000))
