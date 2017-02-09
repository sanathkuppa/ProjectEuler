# -1 means unevaluated
# 1 means a 1 cycle
# 89 means a 89 cycle

def Squares(n):
    List = list(str(n))
    Sum  = 0
    for i in List:
        Sum += int(i)*int(i)
    return(Sum)

Lim     = 10000001
Arr     = [-1]*Lim
Arr[1]  = 1
Arr[89] = 89
Cou = 0

for i in range(1,Lim):
    Temp = i
    Sq   = Squares(Temp)

    while True:
        if Arr[Sq] == 89:
            Arr[i] = 89
            break
        elif Arr[Sq] == 1:
            Arr[i] = 1
            break
        else:
            Temp = Sq
            Sq   = Squares(Temp)

for i in Arr:
    if i == 89:
        Cou+=1


print(Cou)
