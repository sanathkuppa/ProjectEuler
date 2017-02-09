f = open('Problem_11.txt', 'r')

A = []
B = []

for line in f:
    A.append(line.split(' '))

for i in A:
    y = []
    for x in i:
        y.append(int(x))
        
    B.append(y)

print(B) #B has an array of arrays of the required numbers

maxi = -1

# Get all the possible products
for j in range(len(B[0])):
    for i in range(len(B[0])-3):
        product = B[j][i]*B[j][i+1]*B[j][i+2]*B[j][i+3]

        if product > maxi:
            maxi = product

        product = B[i][j]*B[i+1][j]*B[i+2][j]*B[i+3][j]
        
        if product > maxi:
            maxi = product


for j in range(len(B[0])-3):
    for i in range(len(B[0])-3):
        product = B[j][i]*B[j+1][i+1]*B[j+2][i+2]*B[j+3][i+3]

        if product > maxi:
            maxi = product

        product = B[j+3][i]*B[j+2][i+1]*B[j+1][i+2]*B[j][i+3]
        
        if product > maxi:
            maxi = product

print(maxi)
