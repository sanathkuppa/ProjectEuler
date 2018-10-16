def Expr1(x):
    return((3*x+1)*(x-1))
    
def Expr2(x):
    return((3*x-1)*(x+1))

Limit = 10000000

Root    = 1
Current = 2 
Total   = 0

while((3*Current+1)<=Limit):
#    Value = Expr1(Current)
    Value = (3*Current+1)*(Current-1)
    if Value < Root*Root:
        Current = Current + 1
    elif Value > Root*Root:
        Root = Root + 1
    else:
        Total = Total + 3*Current + 1
        Root  = Root + 1
        Current = Current + 1
        
Root    = 1
Current = 2  

while((3*Current-1)<=Limit):
#    Value = Expr2(Current)
    Value = (3*Current-1)*(Current+1)
    if Value < Root*Root:
        Current = Current + 1
    elif Value > Root*Root:
        Root = Root + 1
    else:
        Total = Total + 3*Current - 1
        Root  = Root + 1
        Current = Current + 1


print(Total)
