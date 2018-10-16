def Factorial(Number):
    # Copy of all the factorials for speed
    Array = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
    return(Array[Number])

def Function(Number):
    Sum     = 0
    Array   = list(str(Number))
    for i in Array:
        Sum = Sum + Factorial(int(i))
    return(Sum)
    
def Chain(Number):
    Output = []
    Flag   = True
    Curr   = Number
    
    while Flag:
        if Curr in Output:
            Flag = False
            break
        else:
            Output.append(Curr)
            Curr = Function(Curr)
    
    return(Output)
    
def Filling(Limit):
    Curr = 1
    Main = {}
    Count = 0
    
    while Curr <= Limit:
        if Curr not in Main:
            List = Chain(Curr)
            Size = len(List)
            for i in List:
                Main[i] = Size
                Size    = Size - 1

        Curr = Curr + 1

    for i in range(1,Limit+1):
        if Main[i] == 60:
            Count = Count + 1
            
    print(Count)


Filling(1000000)
