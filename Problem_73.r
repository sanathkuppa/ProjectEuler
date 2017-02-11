Limit = 12000
Prim  = vector()
Test  = rep(1,Limit)
for(i in c(2:Limit)){
  if(Test[i]==1){ #Prime
    Prim <- c(Prim,i)
    Sum = 2*i
    while(Sum<=Limit){
      Test[Sum] <- 0
      Sum <- Sum + i
    }
  }
}

Prim
Sum  = 0
for(q in c(1:Limit)){
  Den   = q
  if(Den%%500==0){
    print(Den)
  }
  Lower = floor(Den/3)+1
  Upper = ceiling(Den/2)-1
  Array <- vector()
  Check <- vector()
  if(Lower <= Upper){
    Array = c(Lower:Upper)
    Check = rep(1,length(Array))
    
    for(i in Prim){
      if(Den%%i==0){
        for(j in c(1:length(Array))){
          if(Array[j]%%i==0 && Array[j] != i){
            Check[j] = 0
          }
        }
      }
    }

    Sum = Sum + sum(Check)
  }
}

print(Sum)
