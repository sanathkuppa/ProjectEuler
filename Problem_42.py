f = open('Problem_42.txt', 'r')

# All possible triangular numbers
def Possible(n):
    A = []
    for i in range(n):
        A.append((i+1)*(i+2)/2)
    return(A)

A = []
C = []

## Load the data into an array
for line in f:
    A = line.split(',')


## Remove the "" at the start and end
for Temp in A:
    C.append(Temp[1:-1])

Coun = 0
Vals = []
Pos  = Possible(30)

# Get a list of all the Vals
for Word in C:
    Val    = 0
    for Letter in Word:
        ## The ascii number for A is 65. So subtracting 64 from everything
        Val += ord(Letter)-64
    Vals.append(Val) 

for i in Pos:
    Coun += Vals.count(i)
    print(Vals.count(i))

print(Coun)
    
