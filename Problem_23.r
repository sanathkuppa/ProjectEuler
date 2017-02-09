n = 28123
FactorSum <- rep(0,n)

for(x in c(1:n)){
  for(y in c(1:x)){
    if(x%%y == 0){
      FactorSum[x] = FactorSum[x] +y
    }
  }
}

AbList <- vector()
for(x in c(1:n)){
  if(FactorSum[x]>2*x){
    AbList <- c(AbList,x)
  }
}

Array <- rep(0,n)

Sum <- 0
for(x in AbList){
  for(y in AbList){
    Array[x+y] = 1
  }
}

for(x in c(1:n)){
  if(Array[x]==0){
    Sum = Sum +x
  }
}

print(Sum)
