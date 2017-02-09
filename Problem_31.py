Sum = 200

# We need to define the number of 200,100,50,20,10,5 and 2.
# The number of 1s is dependent on the others

Den = [200,100,50,20,10,5,2]

def Tot(Sum,Pos):
    Possibilities = 1 + (Sum//Den[Pos])
    Count = 0

    if Pos == len(Den)-1:
        return Possibilities
    else:
        for i in range(Possibilities):
            Rem = Sum - Den[Pos]*i
            Count += Tot(Rem,Pos+1)

        return Count

print(Tot(200,0))
