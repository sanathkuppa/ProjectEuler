Limit <-  35000
n <- c(2:Limit)
n <- n[n%%2==1]

Array  <- vector()
PrmChk <- rep(1,4*length(n))

for(i in n){
  Num1  <- i*i
  Num2  <- i-1
  Array <- c(Array,c(Num1,Num1-Num2,Num1-2*Num2,Num1-3*Num2))
}

Test  <- rep(1,Limit)
Test[1] <- 0

for(i in c(2:Limit)){
  if(Test[i]==1){ #Prime
    Sum = 2*i
    while(Sum<=Limit){
      Test[Sum] <- 0
      Sum <- Sum + i
    }
    for(j in c(1:length(Array))){
      if(Array[j]%%i==0){
        if(Array[j]>i){
          PrmChk[j]=0
        }
      }
    }
  }
}

Prime = 0
NotPrime = 1
MinRatio = 1
for(i in c(1:length(n))){
  PrimeCount <- 0
  Num1  <- i*i
  Num2  <- i-1
  PrimeCount <- PrmChk[4*i-3] + PrmChk[4*i-2] +PrmChk[4*i-1] +PrmChk[4*i]
  Prime <- Prime + PrimeCount
  NotPrime <- NotPrime + 4 - PrimeCount
  Ratio <- Prime/(Prime+NotPrime)
  MinRatio <- min(MinRatio,Ratio)
  if(Ratio <= 0.1){
    print(n[i])
    break
  }
}
