Numbers = []

for i in range(2,101):
    for j in range(2,101):
        Numbers.append(i**j)

Numbers.sort()

## print(Numbers)

Prev = -30
Coun = 0

## If the current number is same as previous don't increase the count
for i in Numbers:
    if i != Prev:
        Coun += 1
    Prev = i

print(Coun)
