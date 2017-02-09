# If the perimeter is atmost 1000, the hypotenuse is less than 500
from math import sqrt

Squares = []
Dummy   = []

for i in range(1,501):
    Squares.append(i*i)

for j in range(1,2000):
    Dummy.append(0)

List = []

for i in range(len(Squares)):
    for j in range(i):
        if Squares[i]/2 < Squares[j]:
            Req = Squares[i]-Squares[j]
            if Squares.count(Req):
                Temp = []
                Temp.append(Req)
                Temp.append(Squares[j])
                Temp.append(Squares[i])
                List.append(Temp)

for i in List:
    Sum = 0
    for j in i:
        Sum += sqrt(j)
    Dummy[int(Sum)] += 1

Max = -1
Ind = -1

for i in range(1,1001):
    if Max < Dummy[i]:
        Max = Dummy[i]
        Ind = i

print(Max)
print(Ind)
