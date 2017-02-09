# The 2 numbers to be multiplied and the product together should have 9 digits
# The only possiblity is one number has 2 digits, the other number has 3 digits
# and the product has 4 digits

List = []
Sum  = 0

for i in range(1,10000):
    for j in range(1,int(10000/i)): #To ensure 4 digits
        prod = i*j
        Dig  = list(str(i))
        Dig.extend(list(str(j)))
        Dig.extend(list(str(prod)))
        Dig.sort()

        if Dig == [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]:
            print(i)
            print(j)
            print(prod)
            List.append(prod)

List.sort()
print(List)

Prev = -32

for i in List:
    if Prev != i:
        Sum += i
        Prev = i


print(Sum)
