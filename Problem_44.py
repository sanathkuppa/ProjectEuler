from math import sqrt

def Pentagon(n):
    return(int(n*(3*n-1)/2))
    
def Solution(n):
    Out = (1 + sqrt(1 + 4*3*2*n))/6
    return(Out)
    
for i in range(1,10000):
    for j in range(1,i):
        Sum = Pentagon(i) + Pentagon(j)
        if(Pentagon(int(Solution(Sum)))==Sum):
            Diff = Pentagon(i) - Pentagon(j)
            if(Pentagon(int(Solution(Diff)))==Diff):
                print(Diff)
