mydata1 = read.table("Problem_59.txt",as.is = TRUE)
mydata2 = mydata1$V1
mydata3 = strsplit(mydata2,',')
totdata = numeric()

for(i in 1:length(mydata3[[1]])){
  temp <- mydata3[[1]][i]
  data = as.integer(temp)
  totdata <- c(totdata,data)
}

Group1 = vector()
Group2 = vector()
Group3 = vector()

for(i in 1:length(totdata)){
  if(i%%3==1){
    Group1 = c(Group1,totdata[i])
  }else if(i%%3 == 2){
    Group2 = c(Group2,totdata[i])
  }else{
    Group3 = c(Group3,totdata[i])
  }
}

Space = 32
SpASC = intToBits(Space)

Group1Code = as.numeric(names(sort(table(Group1),decreasing = TRUE)[1]))
Group1CASC = intToBits(Group1Code)
Group1Key  = xor(SpASC,Group1CASC)

Sum  = 0
Blah = vector()

for(i in Group1){
  Bits = intToBits(i)
  New  = xor(Bits,Group1Key)
  Rev  = rev(New)
  Num  = unbinary(paste(as.numeric(Rev), collapse=""))
  Sum  = Sum + Num
  Blah = c(Blah,Num)
  
}

Group2Code = as.numeric(names(sort(table(Group2),decreasing = TRUE)[1]))
Group2CASC = intToBits(Group2Code)
Group2Key  = xor(SpASC,Group2CASC)

for(i in Group2){
  Bits = intToBits(i)
  New  = xor(Bits,Group2Key)
  Rev  = rev(New)
  Num  = unbinary(paste(as.numeric(Rev), collapse=""))
  Sum  = Sum + Num
  Blah = c(Blah,Num)
}

Group3Code = as.numeric(names(sort(table(Group3),decreasing = TRUE)[1]))
Group3CASC = intToBits(Group3Code)
Group3Key  = xor(SpASC,Group3CASC)

for(i in Group3){
  Bits = intToBits(i)
  New  = xor(Bits,Group3Key)
  Rev  = rev(New)
  Num  = unbinary(paste(as.numeric(Rev), collapse=""))
  Sum  = Sum + Num
  Blah = c(Blah,Num)
}

print(Sum)
