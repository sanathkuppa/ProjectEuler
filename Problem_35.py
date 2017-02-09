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

# Get all the digits for the number
def Digits(n):
    A = []
    while n>0:
        A.append(n%10)
        n = n//10
    A.reverse()
    return A

def Rotated(A):
    C = []
    C.append(A[-1])
    A.pop()

    for i in A:
        C.append(i)

    return(C)

def AllRot(n):
    Dig = Digits(n)
    Tot = []
    Tot.append(n)
    Tem = Rotated(Dig)
    C   = 1
    
    while C<6:
        C +=1 
        Tot.append(Number(Tem))
        A   = Number(Tem) #No idea why
        Tem = Rotated(Tem)
        
    return Tot

# Convert the number to the digits
def Number(A):
    Sum = 0
    A.reverse()
    for i in range(len(A)):
        Sum += A[i]*(10**i)
    return Sum

Count = 0
P   = primes(1000000)
for i in range(2,1000000):
    A = AllRot(i)
    C = 0
    for j in A:
        if P[j]:
            C += 1

    if C == 6:
        print(i)    
        Count += 1

print(Count)
