from math import sqrt

def PrimeArray(n):
    from math import sqrt

    A,B,C = [],[],[]

    for i in range(int(n+1)):
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
        for var in range(int(loopcount)):
            B[(a*(var+2))] = 0
    return(B)

def Primes(n):
    B = PrimeArray(n)
    C = []
    for var in range(len(B)):
        if B[var] == 1:
            C.append(var)

    return(C)

Primes = Primes(10000)
Array  = PrimeArray(10000)
for i in range(len(Primes)):
    for j in range(0,i):
        Prime1 = Primes[i]
        Prime2 = Primes[j]
        Mid    = int((Prime1 + Prime2)/2)

        if Array[int(Mid)] == 1: #Numbers form an AP
            Str1 = list(str(Prime1))
            Str2 = list(str(Prime2))
            StrM = list(str(Mid))
            Str1.sort()
            Str2.sort()
            StrM.sort()
            if Str1 == Str2:
                if Str1 == StrM:
                    print(Prime1)
                    print(Prime2)
                    print(Mid)
