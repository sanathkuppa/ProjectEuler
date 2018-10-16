Test = {}
for i in range(1,100000):
    String       = ("".join(sorted(str(i**3))))
    if String in Test:
        Current      = Test[String]
        Current.append(i**3)
        Test[String] = Current
    else:
        Test[String] = [i**3]

Array = []
for key,value in Test.items():
    if(len(value)==5):
        Array.append(value[0])
        
Array.sort()
print(Array[0]I
