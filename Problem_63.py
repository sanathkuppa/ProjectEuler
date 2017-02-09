# The base has to be <10.. Else, the nth power has atleast n+1 digits

Cou = 0

for base in range(1,10):
    Pow = 1
    while(len(str(base**Pow)) == Pow):
        Cou += 1
        Pow += 1

print(Cou)
