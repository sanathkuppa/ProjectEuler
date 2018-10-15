def Count(Number):
    Root  = math.ceil(sqrt(Number))
    Count = 0;
    for Divisor in range(2,Root):
        if(Number%Divisor == 0):
            Quotient = int(Number//Divisor)
            A = (Quotient + Divisor)/2
            B = (Quotient - Divisor)/2
            
            if((A%2==0) & (B%2==0)):
                Count = Count + 1
#                print([Number,A,B])
            if((A%2==1) & (B%2==1)):
                Count = Count + 1
#                print([Number,A,B])
            
    return(Count)
    
def Main(Number):
    Sum = 0;
    for i in range(2,Number+1):
        Sum = Sum + Count(i)
    return(Sum)

print(Main(1000000))
