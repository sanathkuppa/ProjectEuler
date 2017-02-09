for Den in range(11,100):
    DenTen = Den//10
    DenOne = Den%10
    for Num in range(11,Den):
        NumTen = Num//10
        NumOne = Num%10

        if DenTen == NumOne:
            if DenOne != 0:
                if NumTen/DenOne == Num/Den:
                    print(Num)
                    print(Den)
            
        if DenOne == NumTen:
            if NumOne/DenTen == Num/Den:
                print(Num)
                print(Den)
