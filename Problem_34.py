## 7*(fact(9)) is 2540160. So, if the number has 8 digits,
## the sum cant ever be 8 digits

def Factorial(n):
    if n == 0:
        return(1)

    if n == 1:
        return(1)

    return(n*Factorial(n-1))

Facts = []

for i in range(20):
    Facts.append(Factorial(i))

Upper = 2540160
Ans   = 0
for i in range(1,Upper):
    Num    = i
    Sum    = 0
    while Num > 0:
        Digit = Num%10
        Num   = Num//10
        Sum  += Facts[Digit]
    if Sum == i:
        print(Sum)
        Ans += Sum

