n = 100
Array = [1 for i in range(n)]
Array[0] = 2

for i in range(33):
  Array[3*i+2] = 2*i+2


Range = range(n-1)
Range.reverse()

Num = 1
Den = Array[n-1]
for i in Range:
    DenNew = Den*Array[i]+Num
    NumNew = Den
    Num = NumNew
    Den = DenNew
    print Den
    
    
print sum(map(int,list(str(Den))))
