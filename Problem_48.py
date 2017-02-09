Sum = 0

## No need for any comments. Thanks to insane computing skills!
for i in range(1000):
    num   = i+1
    tot   = (num**num)%(10**11)
    Sum  += tot

print(Sum%(10**10))
