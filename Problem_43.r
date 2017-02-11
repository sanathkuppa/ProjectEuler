# 17 divisibility
a <- c(0:999)
a <- a[a%%17==0]
a <- sprintf("%03d",a)
b <- vector()
for(i in a){
  if(max(unname(table(strsplit(i,""))))==1){
    b <- c(b,strtoi(i,10))
  }
}
a <- b

filter <- function(Array,Power,Prime,String){
  NewArr <- vector()
  for(i in c(0:9)){
    for(j in Array){
      Num <- (i*10^Power)+j
      Str <- sprintf(String,Num)
      if((Num%/%(10^(Power-2)))%%Prime == 0){
        if(max(unname(table(strsplit(Str,""))))==1){
          NewArr <- c(NewArr,Num)
        }
      }
    }
  }
}

a1 <- filter(a,3,13,"%04d")
a2 <- filter(a1,4,11,"%05d")
a3 <- filter(a2,5,7,"%06d")
a4 <- filter(a3,6,5,"%07d")
a5 <- filter(a4,7,3,"%08d")
a6 <- filter(a5,8,2,"%09d")

NewArr <- vector()
for(i in c(1:9)){
  for(j in a6){
    Num <- (i*10^9)+j
    Str <- toString(Num)
    if(max(unname(table(strsplit(Str,""))))==1){
      NewArr <- c(NewArr,Num)
    }
  }
}

print(sum(NewArr))  
