N   = 100
Arr = matrix(0,nrow = N, ncol = N)

# If you use all 1's, there is only 1 to get each number
Arr[1,1] = 1
for(i in 2:N){
  Arr[1,i] = 1
}

Arr 

for(Sum in 1:N){
  for(Max in 2:N){
    if(Max > Sum){
      Arr[Max,Sum] = Arr[Sum,Sum]
    }else if(Max == Sum){
      Ans = 0
      for(i in 1:(Max-1)){
        Ans = Ans + Arr[i,Sum-i]
      }
      Ans = Ans + 1
      Arr[Max,Sum] = Ans
    }else{
      Ans = 0
      for(i in 1:(Max)){
        Ans = Ans + Arr[i,Sum-i]
      }
      Arr[Max,Sum] = Ans
    }
  }
}

print(Arr[N-1,N])
