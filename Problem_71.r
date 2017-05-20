N = 1000
Arr = vector()
for(i in 1:N){
  Arr = c(Arr,(i*3)%/%7)
  if((i*3)%%7 == 0){
    Arr[i] = Arr[i]-1
  }
}

Max = -1
for(i in 1:N){
  if(Arr[i]/i > Max){
    Max = Arr[i]/i
    print(Arr[i])
  }
}

# By testing for small values of N, a pattern can easily be seen
# It can be shown that the answer is the largest k such that k < N*3/7 and k %%3 = 2

# Initial Guess
Answer = (1000000*3)%/%7
print(Answer)
print(Answer%%3)

Answer = Answer - 1
print(Answer)
print(Answer%%3)
