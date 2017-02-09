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
            
    return(B)

def Value(n,a,b):
    return((n*n)+(a*n)+b)

Max = -22
a   = -3000
b   = -3000
Pr  = primes(50000)

for i in range(-1000,1001):
    for j in range(-1000,1001):
        n = 0
        while(Pr[Value(n,i,j)]):
            n += 1

        if n>Max:
            Max = n
            a   = i
            b   = j

print(Max)
print(a)
print(b)
            
