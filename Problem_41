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


def Pandig(n):
    List = []
    for i in range(n):
        List.append(str(i+1))
    return(List)

# The biggest pandigitial prime would not have 8 or 9 digits as it would
# not be a prime (Sum of digits would be divisible by 3)
Primes = primes(10000000)

for i in Primes:
    Str = list(str(i))
    Str.sort()
    Len = len(Str)
    if Str == Pandig(Len):
        print(i)
