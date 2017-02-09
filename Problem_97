def Binary(n):
    List = []

    while n>0:
        List.append(n%2)
        n = n//2

    List.reverse()
    return List

Bin      = Binary(7830457)
DigCount = len(Bin)
Array    = []
Array.append(2)
Prod     = 1

for i in range(1, DigCount):
    Prod = Array[i-1]**2
    Prod = Prod%(10**11)
    Array.append(Prod)

Array.reverse()

Ans = 1
for i in range(DigCount):
    Ans *= Array[i]**Bin[i]
    

Ans *= 28433
Ans += 1

print(Ans%(10**10))
