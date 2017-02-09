A = []
B = [31,28,31,30,31,30,31,31,30,31,30,31] #Dictionary of days each month
S = 0

for i in range(100):
    C = []
    for j in range(12):
        if j != 1: #Feb
            C.append(B[j])
        else: #Feb
            Year = i + 1901
            if Year%400 == 0:
                C.append(29)
            elif Year%100 == 0:
                C.append(28)
            elif Year%4 == 0:
                C.append(29)
            else:
                C.append(28)
    A.append(C)

print(A)

# Now go through every month to get the number of sundays

Sum = 0
#Zero is monday. Any number that divides with 7 with remainder 6 means
#it starts with sunday

for i in A:
    for j in i:
        Sum += j
        if Sum % 7 == 5:
            S += 1

print(S)
