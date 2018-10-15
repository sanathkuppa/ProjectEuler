def Factorial(Number):
    # Copy of all the factorials for speed
    Array = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
    return(Array[Number])

def Choose(n,r):
    return(int(Factorial(n)/(Factorial(n-r)*Factorial(r))))  

def Series(Base,Size,Index):
    
    Output = []
    
    Current     = 0
    Selected    = 0
    Total       = Index
    
    # If we have to choose r out of n and the first number is set, there
    # (n-1)C(r-1) ways
    
    # The idea is to see if the index is small enough that the given Current
    # would be selected, else increment the current and reduce the index 
    # accordingly
    
    while Current<Base:
        if Choose(Base-Current-1,Size-Selected-1) <= Total:
            Total    = Total - Choose(Base-Current-1,Size-Selected-1)
        else:
            Selected = Selected + 1
            Output.append(Current)
            
        Current = Current + 1
        
    return(Output)
    
def Possible(Array1,Array2,Number):
    # 6 and 9 are equivalent. So modify the arrays accordingly
    if (6 in Array1) & (9 not in Array1):
        Array1.append(9)
    elif (9 in Array1) & (6 not in Array1):
        Array1.append(6)
        
    if (6 in Array2) & (9 not in Array2):
        Array2.append(9)
    elif (9 in Array2) & (6 not in Array2):
        Array2.append(6)
    
    if (Number[0] in Array1) & (Number[1] in Array2):
        return(1)

    if (Number[0] in Array2) & (Number[1] in Array1):
        return(1)
    
    return(0)
    
def Include(Array1,Array2):
    
    Candidates  = [[0,1],[0,4],[0,9],[1,6],[2,5],[3,6],[4,9],[6,4],[8,1]]
    Output      = 1
    
    for i in Candidates:
        if not Possible(Array1,Array2,i):
            return(0)
            
    return(1)
    
Sum = 0
for i in range(210):
    for j in range(i+1):
        Sum = Sum + Include(Series(10,6,i),Series(10,6,j))
        
print(Sum)


#print(Series(5,2,3))    
#print(Series(4,2,3))
#print(Choose(10,6))
#print(Include([0,5,6,7,8,9],[1,2,3,4,6,7]))
