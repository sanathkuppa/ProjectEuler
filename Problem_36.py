# Upper limit of 1 million -> 20 digits in binary

## Generate an array of all the possible numbers of a number of digits
## Do this by taking all the numbers of smaller size and appending 0 or 1
def Numbers(n): 
    if n == 1:
        Out = []
        Out.append([0])
        Out.append([1])
    else:
        Out = []
        Prev0 = Numbers(n-1)
        Prev1 = Numbers(n-1)
        for i in range(len(Prev1)):
            Prev0[i].append(0)
            Out.append(Prev0[i])
            Prev1[i].append(1)
            Out.append(Prev1[i])
    return Out

## Return all the palindromes..  Note that numbers starting with 0 dont count
def Palindromes(n):
    Out = []
    Num1 = Numbers(n)
    Num2 = Numbers(n)
    for i in range(len(Num1)):
        if Num1[i][0] == 0:
            continue
        else:
            Temp = Num1[i]
            Temp.reverse()
            if Num2[i] == Temp:
                Out.append(Temp)
    return Out

## Returns the decimal corresponding to a binary number
def Decimal(A):
    Sum = 0
    for i in range(len(A)):
        Sum += A[i]*(2**i)
    return Sum

## Checks if the decimal number is a palindrome
def Digits(n):
    A = []
    while n>0:
        A.append(n%10)
        n = n//10
    A.reverse()
    return A

def IsPali(n):
    if n==0:
        return False

    if n>10**6:
        return False
    
    A = Digits(n)
    B = Digits(n)
    B.reverse()
    return A==B

Sum = 0

for i in range(1,21):
    Cand = Palindromes(i)
    for j in Cand:
        if IsPali(Decimal(j)):
            print(Decimal(j))
            Sum+= Decimal(j)

print(Sum)
