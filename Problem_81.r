index <- c(1:80)

mydata1 = read.table("Problem_81.txt",as.is = TRUE)
mydata2 = mydata1$V1
mydata3 = strsplit(mydata2,',')
totdata = numeric()
for(i in index){
  temp <- mydata3[[i]]
  data = as.integer(temp)
  totdata <- c(totdata,data)
}

totmat  <- matrix(totdata,nrow = 80, ncol = 80)
totres  <- matrix(rep(0,6400),nrow = 80, ncol = 80)
array    <- c(2:80)
totres[1,1] <- totmat[1,1]

for(i in array){
  totres[1,i] <- totres[1,i-1]+totmat[1,i]
  totres[i,1] <- totres[i-1,1]+totmat[i,1]
}

for(i in array){
  for(j in array){
    totres[i,j] <- min(totres[i-1,j],totres[i,j-1])+totmat[i,j]
  }
}

print(totres[80,80])
