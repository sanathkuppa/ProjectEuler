Limit <-  500000
Test  <- rep(0,Limit)
 
for(i in c(2:Limit)){
 if(Test[i]==0){ #Prime
   Sum = 2*i
   while(Sum<=Limit){
     Test[Sum] <- Test[Sum]+1
     Sum <- Sum + i
   }
 }
}

for(j in c(2:Limit)){
  if(Test[j]==4){
    if(Test[1+j]==4){
      if(Test[2+j]==4){
        if(Test[3+j]==4){
          print(j)
          break
        }
      }
    }
  }
}
