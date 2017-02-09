f = open( 'Problem_18.txt', 'r' )

A = []
B = []
C = []

for line in f:
    A.append(line.split(' '))

for i in A:
    y = []
    for x in i:
        y.append(int(x))
        
    B.append(y)

for i in range(len(B)):
    y = []
    if i == 0:
        y = B[0]
    else:
        for j in range(i+1):
            y.append(B[i][j] + max(C[i-1][max(0,j-1)], C[i-1][min(j,i-1)]))

    C.append(y)

print(max(C[-1]))
        
