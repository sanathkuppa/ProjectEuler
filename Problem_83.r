mydata1 = read.table("Problem_83.txt",as.is = TRUE)
mydata2 = mydata1$V1
mydata3 = strsplit(mydata2,',')
Data    = matrix(0,nrow = 80,ncol = 80)
for(i in 1:80){
  Data[i,] = as.integer(mydata3[[i]])
}

# Indicator matrix to see if the shortest distance from a node to the bottom right is known
Loc      = matrix(0,nrow = 80, ncol = 80)
Loc[80,80] = 1

# This matrix holds the shortest distance from al nodes to the bottom right
Ans        = matrix(1e10,nrow = 80, ncol = 80)
Ans[80,80] = Data[80,80]

# Implement Djkstra's Algo
while(Loc[1,1] == 0){
  NextRow  = -1
  NextCol  = -1
  NextDist = 1e9
  Temp     = Ans
  
  for(i in 1:80){
    for(j in 1:80){
      if(Loc[i,j] == 0){
        if(i != 1){
          Temp[i,j] = min(Temp[i,j],Temp[i-1,j]+Data[i,j])
        }
        if(i != 80){
          Temp[i,j] = min(Temp[i,j],Temp[i+1,j]+Data[i,j])
        }
        if(j != 1){
          Temp[i,j] = min(Temp[i,j],Temp[i,j-1]+Data[i,j])
        }
        if(j != 80){
          Temp[i,j] = min(Temp[i,j],Temp[i,j+1]+Data[i,j])
        }
      }
    }
  }
  
  for(i in 1:80){
    for(j in 1:80){
      if(Loc[i,j] == 0){
        if(Temp[i,j] < NextDist){
          NextRow  = i
          NextCol  = j
          NextDist = Temp[i,j]
        }
      }
    }
  }
  
  Loc[NextRow,NextCol] = 1
  Ans[NextRow,NextCol] = NextDist
  if(sum(Loc)%%20 == 0){
    print(sum(Loc))
  }
}

# Final Answer
print(Ans[1,1])
