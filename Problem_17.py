def ToWords(n):
    Ones  =  [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
    Tens  =  [ "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    Hund  = "hundred"
    And  = "and"

    Word = ""
    Word += Ones[n//100]

    if n//100:
        Word += Hund

        if n%100:
            Word += And
            
    if n%100//10 > 1:
        Word += Tens[n%100//10]

    if n%100//10 == 1:
        Word += Ones[n%100]
    else:
        Word += Ones[n%10]
        
    return Word

Sum = 0
for i in range(1000):
    Sum += len(ToWords(i))

Sum += len("onethousand")

print(Sum)
