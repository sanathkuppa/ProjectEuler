f = open('Problem_13.txt', 'r')

A = []
B = []

for line in f:
    A.append(int(line))

for i in A:
    B.append(i//10**35)

print(sum(B))

