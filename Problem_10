from math import sqrt

Target = 2000000

A = []
B = []
Sum = 0

for i in range(Target+1):
    A.append(i) #Initialize A, from 0 to 2000000
    B.append(1) #Initialize B, containing all 1s from 0 to 2000000

# Remove 0 and 1 from A
A.reverse()
A.pop()
A.pop()
A.reverse()

root = sqrt(Target) #Enough to check until root(i)
tot  = -1 #1 is added to the sum later, so remove it

for a in A:
    # Check until root(i)
    if a > root:
        break
    
    #  Remove all the multiples of A
    loopcount = Target//a
    loopcount -= 1

    # Just to see the status
    print(loopcount)

    # Remove the number from the list
    for var in range(loopcount):
        B[(a*(var+2))] = 0

# Look for all the primes.. Remember 1 is set to prime..
# So take it out from the sum later
for i in range(len(B)):
    if B[i] == 1:
        tot += i

print(tot)
