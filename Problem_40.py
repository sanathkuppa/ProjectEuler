def Digits(n):
    A = []
    while n>0:
        Digit = n%10
        n     = n//10
        A.append(Digit)
    A.reverse()
    return A
        
def Answer(n):
    A         = []
    Count     = 0
    DigitSum  = 0
    A.append(0)
    
    while DigitSum < n+10:
        Count    += 1
        Dig       = Digits(Count)
        DigitSum += len(Dig)
        for i in Dig:
            A.append(i)
    return(A)

p = Answer(1000000)
print(p[1]*p[10]*p[100]*p[1000]*p[10000]*p[100000]*p[1000000])
