def Choose(n,r):
    if r == 0:
        return 1
    else:
        return Choose(n,r-1)*(n-r+1)/r


Count = 0
for n in range(2,101):
    for r in range(n):
        if Choose(n,r) >= 10**6:
            Count += 1


print(Count)
