f = open('Problem_22.txt', 'r')

A = []
C = []

## Load the data into an array
for line in f:
    A = line.split(',')


## Remove the "" at the start and end
for Temp in A:
    C.append(Temp[1:-1])

C.sort()

Sum     = 0
Count   = 0

for Word in C:
    Count += 1
    Prod   = Count
    Val    = 0
    
    for Letter in Word:
        ## The ascii number for A is 65. So subtracting 64 from everything
        Val += ord(Letter)-64

    Prod  *= Val
    Sum   += Prod

print(Sum)
