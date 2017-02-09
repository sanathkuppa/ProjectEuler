## 6*(9**5) is 354294. So, if the number has 7 digits,
## the sum cant ever be 7 digits

Upper = 354294
Ans   = 0
for i in range(1,Upper):
    Num    = i
    Sum    = 0
    while Num > 0:
        Digit = Num%10
        Num   = Num//10
        Sum  += Digit**5
    if Sum == i:
        print(Sum)
        Ans += Sum

print(Ans-1) ## Because we don't need 1
