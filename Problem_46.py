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


Limit = 10000
Array = PrimeArray(Limit)


for i in range(3,Limit,2):
    if Array[i] == 0: #if composite
        Temp  = i
        Count = 1
        IsAns = 1
        while Temp > 0:
            Temp = i - (2*Count*Count)
            if Array[Temp]: #Diff of comp and 2*x^2 is a prime
                IsAns = 0
                break
            Count += 1

        if IsAns:    
            print(i)
        
