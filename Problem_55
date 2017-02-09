Count = 0

def Rev(n):
    Str = list(str(n))
    Str.reverse()
    Ans = ""
    for i in Str:
        Ans += i

    return int(Ans)

def IsPali(n):
    Str1 = list(str(n))
    Str2 = list(str(n))
    Str2.reverse()

    return Str1 == Str2

Ans = 0
for i in range(1,10001):
   Count = 0
   Temp  = i
   while Count < 50:
       rev   = Rev(Temp)
       chk   = rev+Temp
       Temp  = chk
       Count += 1
       
       if IsPali(chk):
           Ans += 1
           break

print(10000-Ans)
       
