def Bouncy(n):
    Str = str(n)
    Ass = "".join(sorted(Str))
    Lis = list(Ass)
    Rev = reversed(Lis)
    Des = "".join(Rev)

    if((Str == Ass) | (Str == Des)):
        return(True)
    else:
        return(False)

Limit = 5000000
Boun = 0
NonB = 0
for i in range(1,Limit+1):
    if Bouncy(i):
        Boun = Boun + 1
    else:
        NonB = NonB + 1
    if NonB/(Boun + NonB) == 0.99:
        print(i)
        break

print(NonB/(Boun + NonB))
