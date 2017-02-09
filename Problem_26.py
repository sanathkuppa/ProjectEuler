def Length(n):
    Count = 0
    Arr   = []
    Pow   = 0
    while True:
        Rem = (10**Pow)%n
        
        if Rem == 0:
            return 0

        if Arr.count(Rem) == 1: 
            Prev = Arr.index(Rem)
            return(Pow - Prev)
        
        Arr.append(Rem)
        Pow += 1

Max = -1
Pos = -1
for i in range(2,1001):
    if Length(i) > Max:
        Max = Length(i)
        Pos = i

print(Pos)
