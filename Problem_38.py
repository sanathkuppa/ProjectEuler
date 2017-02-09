# The largest number should not have 5 digits and its double would have
# 5 digits too and we would not get 9 digits

n       = -1
MaxFact = -1


for i in range(1,10000):
    fact = 1
    List = []

    while len(List)<10:
        Num = i*fact
        List.extend(list(str(Num)))
        Temp = List
        Temp.sort()

        if Temp == [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]:
            n       = i
            MaxFact = fact
            break

        fact += 1


for i in range(MaxFact):
    print(n*(i+1))
