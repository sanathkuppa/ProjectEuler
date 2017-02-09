def Collatz(n,A):
    if n == 1:
        A[1] = 1
        return(A)

    if n not in A:
        if n%2 == 0:
            A[n] = 1 + Collatz(int(n/2), A)[int((n/2))]
        else:
            A[n] = 1 + Collatz(int((3*n)+1),A)[int(3*n+1)]
            
    return(A)
    
def main(n):
    A = {}

    for i in range(n):
        Num = n+1-i
        A   = Collatz(Num,A)

    Maxi   = -1
    Ans    = -1
    for i in range(n):
        if i == 0:
            continue
        if A[i] > Maxi:
            Maxi = A[i]
            Ans  = i

    return(Ans)

print(main(1000000))
